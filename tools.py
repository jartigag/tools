#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pip._internal
import json
import sys
import os
import subprocess
#import argparse

__author__ = 'jartigag'
__version__ = '0.1'
__email__ = 'jartigag@pm.me'

def print_index(): #TODO: columns?
    i = json.load(open("tools.json"))
    print(json.dumps(i, indent=2)) #TODO: print numbered list

def choose(o):
    if o=='x':
        print("bye!")
        sys.exit(0)
    else:
        pass

if __name__ == "__main__":

    print('''

                                888888888888                       88             
                                     88                            88             
                                     88                            88             
    88,dPYba,,adPYba,   8b       d8  88   ,adPPYba,    ,adPPYba,   88  ,adPPYba,  
    88P'   "88"    "8a  `8b     d8'  88  a8"     "8a  a8"     "8a  88  I8[    ""  
    88      88      88   `8b   d8'   88  8b       d8  8b       d8  88   `"Y8ba,   
    88      88      88    `8b,d8'    88  "8a,   ,a8"  "8a,   ,a8"  88  aa    ]8I  
    88      88      88      Y88'     88   `"YbbdP"'    `"YbbdP"'   88  `"YbbdP"'  
                            d8'                                                   
                           d8'  {v%s by %s (%s)}
    ''' % (__version__,__author__,__email__))

    print_index()
    o = str(input("(type x to exit)\nchoose a tool by its number: "))
    choose(o)

    '''
    parser = argparse.ArgumentParser(
        description="my tools",
        usage="%(prog)s")

    args = parser.parse_args()
    if not any(vars(args).values()):
        parser.print_help()
    else:
        main()
    '''