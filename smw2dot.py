#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
from logicsym import database


sigtypes = ('unknown','digital','analog','serial')
sigcolors = ('green','blue','red','black')
moduleAPI = [55] # 55 - argument definition
interconnectAPI = [374, 611, 1402, 1540]
# 611 - XPanel, 1540 - TPMC-8L, 1402 - TPMC-8X, 374 - Ethernet ISC


"""
generate stream of tokens
looking like {'a':'b c d', 'e':'f'} for "[\na=b c d\ne=f\n]"
"""
def tokenize(data):
    lines = filter(len, map(lambda x: x.strip(), data.split("\n")))
    for line in lines:
        if line=='[':
            token={}
        elif line==']':
            yield token
        else:
            name,val = line.split('=',1)
            token[name]=val

def get_info(token):
    info = { 'ins':[], 'outs':[], 'params':[], 'comps':[] }
    for i in range(1, int(token.get('mC', 0))+1):
        info['comps'].append(token.get('C%d'%i))
    for i in range(1, int(token.get('mP', 0))+1):
        info['params'].append(token.get('P%d'%i))
    for i in range(1, int(token.get('mI', 0))+1):
        info['ins'].append(token.get('I%d'%i))
    for i in range(1, int(token.get('mO', 0))+1):
        info['outs'].append(token.get('O%d'%i))
    return info

def make_module(name, mtype, ins=[], outs=[], params=[], comps=[], comment=''):
    # prepare - None or integer with offset (smw indexes to python indexes)
    prepare = lambda x: (x is not None) and int(x) or None
    ready_ins = map(prepare, ins)
    ready_outs = map(prepare, outs)
    if comment != '':
        comment = '\\n'+comment

    return {
        'name': name,
        'type': mtype,
        'ins': ready_ins,
        'outs': ready_outs,
        'params': params,
        'comps': comps,
        'comment':comment,
        }

def parse(data):
    header = {}
    signals = {1:('0',0),2:('1',0),3:('Local',0)}
    modules = {}
    for token in data:
        objtype=token.get('ObjTp','')
        
        if objtype=='Hd':
            header['dealer']=token.get('DlrNm','n/a')
            header['programer']=token.get('PgmNm','n/a')
            header['file']=token.get('PrNm','n/a')
            header['hint']=token.get('CltNm','n/a')
            
        elif objtype=='Sg':
            snumber = int(token.get('H', '-1')) # for debug purpose
            sname = token.get('Nm','n/a')
            stype = int(token.get('SgTp','1'))
            if stype not in [1,2,4]:
                stype=0
            elif stype==4:
                stype=3
            signals[snumber]=(sname, stype)

        elif objtype=='Sm':
            mtag = token.get('H', '-1')
            minfo = get_info(token)
            mtype = int(token.get('SmC','-1'))
            mname = token.get('Nm')
            mcomment = token.get('Cmn1','')
            if mname is None:
                mname = database.get(mtype,{}).get('name','!unknown')
            if mtype in moduleAPI:
                module = make_module(mname+" - in", mtype, 
                    [], minfo['ins'], minfo['params'], minfo['comps'], mcomment)
                modules["m"+mtag+"i"] = module
                module = make_module(mname+" - out", mtype, minfo['outs'],
                    comment=mcomment)
                modules["m"+mtag+"o"] = module
            elif mtype in interconnectAPI:
                module = make_module(mname+" - feedback", mtype, 
                    minfo['ins'], [], minfo['params'], minfo['comps'], mcomment)
                modules["m"+mtag+"i"] = module
                module = make_module(mname+" - input", mtype, outs=minfo['outs'],
                    comment=mcomment)
                modules["m"+mtag+"o"] = module
            else:
                module = make_module(
                    mname, mtype, minfo['ins'], minfo['outs'], 
                    minfo['params'], minfo['comps'], mcomment)
                modules["m"+mtag] = module
    return header, signals, modules

def make_dot(header, signals, modules):
    def adv_len(data):
        return len(filter(lambda x: x is not None, data))

    def make_node(tag, item):
        return '  %s [label="%s%s"];'%(tag, item['name'],item['comment'])

    def make_signal(line, name, stype):
        return '  %s -> %s [label="%s", color="%s"];'%(
            line[0],line[1],name, sigcolors[stype])

    def make_signal_bus(line, names, stype):
        return '  %s -> %s [label="%s", color="%s", style="bold"];'%(
            line[0],line[1],"\\n".join(names), sigcolors[stype])

    head = """\
// file: %s
// dealer: %s
// programmer: %s
// hint: %s

digraph {
  //node [shape="record"];
  node [shape="box"];
"""%(header['file'],header['dealer'],header['programer'],header['hint'])
    tail = """}"""
    dot_file = [head]

    checkT = False
    checkF = False
    limit_mods = filter(lambda m: adv_len(modules[m]['ins']) or adv_len(modules[m]['outs']), modules)
    limit_mods.sort()
    for m in limit_mods:
        dot_file.append(make_node(m, modules[m]))
        checkT = 2 in modules[m]['ins'] or checkT
        checkF = 1 in modules[m]['ins'] or checkF
    if checkF:
        dot_file.append('  0 [shape="circle"];')
    if checkT:
        dot_file.append('  1 [shape="circle"];')

    dot_file.append('')

    limit_sigs = filter(lambda s: signals[s][0] not in ['//__digital_reserved__','[~UNUSED~]'], signals)
    actual_sig_lines = set()
    extended_sigs = {}
    #actual_sig_lines.add((src,dst))
    #extended_sigs = { (src,dst):[(name0,type0),(name1,type1)] }
    
    for s in limit_sigs:
        sname, stype = signals[s]
        outs = filter(lambda m: s in modules[m]['outs'], limit_mods)
        if sname == '0':
            outs.append('0')
        if sname == '1':
            outs.append('1')
        
        ins = filter(lambda m: s in modules[m]['ins'], limit_mods)

        pack = set()
        for o in outs:
            for i in ins:
                pack.add((o,i))
        for line in pack:
            actual_sig_lines.add(line)
            if extended_sigs.get(line) is None:
                extended_sigs[line]=[]
            extended_sigs[line].append(signals[s])
            #dot_file.append(make_signal(line,sname,stype))
        #print extended_sigs

    # bus signals agregate
    nonum = lambda name: filter(lambda x: not x.isdigit(), name)
    for asl in actual_sig_lines:
        if len(extended_sigs[asl])==1:
            sname, stype = extended_sigs[asl][0]
            dot_file.append(make_signal(asl,sname,stype))
        else:
            pack = {}
            for n,t in extended_sigs[asl]:
                tag = (nonum(n),t)
                if pack.get(tag) is None:
                    pack[tag]=[]
                pack[tag].append(n)
            for bulk in pack:
                if len(pack[bulk])==1:
                    dot_file.append(make_signal(asl,pack[bulk][0],bulk[1]))
                else:
                    dot_file.append(make_signal_bus(asl,pack[bulk],bulk[1]))
    
    dot_file.append(tail)
    return "\n".join(dot_file)


def main():
    if len(sys.argv) != 2:
        print 'Please specify one filename on the command line.'
        sys.exit(1)

    text = open(sys.argv[1],"rt").read()
    tree = tokenize(text)
    
    header,sigs,mods = parse(tree)
    print make_dot(header,sigs,mods)

if "__main__" == __name__:
    main()

