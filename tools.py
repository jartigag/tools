#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pip._internal
import json
from collections import OrderedDict
import sys
import os
import subprocess
#import argparse

__author__ = 'jartigag'
__version__ = '0.1'
__email__ = 'jartigag@pm.me'

index = json.load(open("tools.json"),object_pairs_hook=OrderedDict)

def print_index(): #TODO: columns?
    i=0
    for category in index:
        i+=1
        print("%i. - \033[4m%s\033[0m" % (i,category.upper()))
        j=0
        for subcat in index[category]:
            j+=1
            print(" \033[1m%i.%i-%s\033[0m" % (i,j,subcat))
            k=0
            print("     [tools]:")
            for tool in index[category][subcat][0]:
                t = tool.rsplit('/',1)
                k+=1
                print("     %i%i%i: %s/\033[1m%s\033[0m" % (i,j,k,t[0],t[1]))
            k=0
            print("     [links]:")
            for link in index[category][subcat][1]:
                k+=1
                print("     %i%i%i: %s" % (i,j,k,link))

def choosed_tool():
    o = str(input("(type x to exit)\nchoose a tool by its number: "))
    try:
        #list indexing start at 0:
        c = int(o[0])-1
        s = int(o[1])-1
        t = int(o[2])-1

        cat = list(index.items())[c][1] # class collections.OrderedDict
        subcat = list(cat.items())[s][1] # class collections.OrderedDict
        tool = subcat[0][t].split('/')[-1] # tool-name from gh.com/u/tool-name

        return tool
    except ValueError:
        if o=='x':
            print("bye!")
            sys.exit(0)
        else:
            print("invalid value")
            choosed_tool()

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
    
    print(choosed_tool())

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