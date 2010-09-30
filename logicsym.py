#!/usr/bin/env python
# -*- coding: utf8 -*-

# TODO: fill with actual data
# make use of inputs and outputs names and params
database = {
    # conditional
    1: {'name':'and'},
    2: {'name':'nand'},
    3: {'name':'or'},
    4: {'name':'nor'},
    5: {'name':'exclusive or'},
    6: {'name':'transition gate'},
    7: {'name':'negative transition gate'},
    20:{'name':'buffer', 'outputs':[], 'inputs':[], 'params':None},
    28:{'name':'truth table'},
    35:{'name':'analog compare'},
    49:{'name':'binary decoder', 'outputs':[], 'inputs':[], 'params':None},
    112:{'name':'exclusive nor'},
    205:{'name':'not', 'outputs':[], 'inputs':[], 'params':None},
    418:{'name':'multiple not'},
    492:{'name':'analog comparison (full set)'},

    # analog operations
    79:{'name':'analog 2\'s offset converter'},
    46:{'name':'analog buffer'},
    114:{'name':'analog div/mod'},
    38:{'name':'analog equate'},
    58:{'name':'analog flip'},
    543:{'name':'analog increment'},
    605:{'name':'analog increment with optional feedback'},
    32:{'name':'analog initialize', 'outputs':[], 'inputs':[], 'params':[]},
    185:{'name':'analog integral'},
    606:{'name':'analog min/max clamp'},
    494:{'name':'analog min/max scaler'},
    31:{'name':'analog non-volatile ramp'},
    23:{'name':'analog preset'},
    22:{'name':'analog ramp'},
    540:{'name':'analog ramp (bounds limited)'},
    66:{'name':'analog rate limiter'},
    24:{'name':'analog scaler'},
    65:{'name':'analog scaler w/o zero pass'},
    538:{'name':'analog scaler w/overflow handling'},
    539:{'name':'analog scaler w/overflow handling w/o zero pass'},
    541:{'name':'analog scaler with i/o limits'},
    47:{'name':'analog scaling buffer'},
    64:{'name':'analog scaling buffer about 50%'},
    45:{'name':'analog step'},
    57:{'name':'analog sum'},
    84:{'name':'analog to digital'},
    122:{'name':'analog value sample'},
    44:{'name':'analog variable preset'},
    547:{'name':'antilog with limits'},
    78:{'name':'decade'},
    61:{'name':'digital sum'},
    85:{'name':'digital to analog'},
    36:{'name':'digital to scaled analog'},
    635:{'name':'double-precision analog initialize'},
    636:{'name':'double-precision analog variable preset'},
    546:{'name':'log with limits'},
    493:{'name':'multiple analog preset'},
    39:{'name':'numeric keypad'},

    # counters
    18:{'name':'binary counter'},
    17:{'name':'ring counter'},
    451:{'name':'ring counter with seed'},

    # debugging
    69:{'name':'analog debugger'},
    472:{'name':'analog force'},
    471:{'name':'digital force'},
    59:{'name':'serial binary to hex'},
    68:{'name':'serial debugger (ascii)'},
    191:{'name':'serial debugger (hex)'},
    470:{'name':'serial force'},
    
    # device interface
    187:{'name':'ascii to kb scan code'},
    437:{'name':'mouse simulator'},
    285:{'name':'virtual serial driver for macro connection'},
    
    # e-control software
    351:{'name':'emailbox'},
    349:{'name':'emailviewer-10 msg inbox'},
    350:{'name':'emailviewer-12 msg inbox'},
    347:{'name':'emailviewer-4 msg inbox'},
    348:{'name':'emailviewer-8 msg inbox'},

    # memory
    34:{'name':'analog ram'},
    221:{'name':'analog ram from database'},
    14:{'name':'d flip flop'},
    90:{'name':'digital ram'},
    120:{'name':'fifo queue'},
    19:{'name':'interlock'},
    419:{'name':'interlock-toggle'},
    15:{'name':'jk flip flop'},
    25:{'name':'memory interlock'},
    186:{'name':'serial memory search'},
    71:{'name':'serial queue'},
    53:{'name':'serial ram'},
    82:{'name':'serial ram from database'},
    12:{'name':'set/reset latch'},
    13:{'name':'toggle'},
    
    # program formatting
    121:{'name':'comment'},
    156:{'name':'subsystem'},
    
    # sequencing operations
    99:{'name':'button presser'},
    98:{'name':'stepper'},
    777:{'name':'stepper with progress & reset'},

    # serial
    77:{'name':'analog to serial'},
    123:{'name':'ascii keypad'},
    54:{'name':'ascii serial decoder'},
    858:{'name':'make string permanent'},
    417:{'name':'make string permanent v1(cuz 3.117 and below'},
    1076:{'name':'send as raw data'},
    56:{'name':'serial buffer'},
    126:{'name':'serial concatenation'},
    86:{'name':'serial demultiplexor'},
    124:{'name':'serial demultiplexor (special)'},
    62:{'name':'serial gether'},
    101:{'name':'serial i/o'},
    236:{'name':'serial memory dialer'},
    125:{'name':'serial multiplexor (special)'},
    73:{'name':'serail pacer'},
    89:{'name':'serial send'},
    63:{'name':'serial substring'},
    1317:{'name':'serial substring (expandable)'},
    1316:{'name':'serial substring w/empty string pass'},
    96:{'name':'serial to analog'},
    72:{'name':'serial/analog one-shot'},
    212:{'name':'telephone dialing keypad'},
    462:{'name':'text append'},

    # system control
    41:{'name':'hard reset'},
    327:{'name':'intersystem communications'},
    102:{'name':'intersystem communications w/offset'},
    192:{'name':'intersystem communications w/status req'},
    40:{'name':'soft reset'},

    # time/date
    438:{'name':'astronomical clock'},
    43:{'name':'clock driver'},
    469:{'name':'extended clock driver'},
    70:{'name':'past'},
    60:{'name':'serialize date'},
    154:{'name':'set system clock'},
    443:{'name':'time offset'},
    74:{'name':'when'},

    # timers
    50:{'name':'debounce'},
    16:{'name':'delay'},
    408:{'name':'logic wave delay'},
    409:{'name':'logic wave pulse'},
    545:{'name':'long delay'},
    21:{'name':'multiple one shots'},
    9: {'name':'one shot'},
    8: {'name':'oscillator'},
    11:{'name':'pulse stretcher'},
    10:{'name':'retriggerable one shot'},
    1309:{'name':'serial/analog logic wave pulse'},
    411:{'name':'variable delay'},
    410:{'name':'variable oscillator'},

    # touchpanel interface
    208:{'name':'indirect text broadcast'},
    
    # system
    55:{'name':'argument definition', 'outputs':[], 'inputs':[], 'params':[]},
    # 155: simpl module
    # 157: dunno
    }
