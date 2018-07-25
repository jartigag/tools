#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#WIP: install_tool(), run_tool()

import pip._internal
import json
from collections import OrderedDict
import sys
import os
import subprocess
import webbrowser

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
                print("     0%i%i%i: %s" % (i,j,k,link))

def choosed_tool():
    msg = "(type: \033[1mx\033[0m to exit, \
\033[1mls\033[0m to see which tools are installed)\n\
choose a tool by its number (start with \033[1m0\033[0m to choose a link):\n>> "
    o = str(input(msg)).lower()
    try:
        #list indexing start at 0:
        c = int(o[0])-1
        if c==-1:
            if len(o)==4:
                c = int(o[1])-1
                s = int(o[2])-1
                t = int(o[3])-1
            else:
                raise IndexError()
        else:
            if len(o)==3:
                s = int(o[1])-1
                t = int(o[2])-1
            else:
                raise IndexError()
        cat = list(index.items())[c][1] # class collections.OrderedDict
        subcat = list(cat.items())[s][1] # class collections.OrderedDict
        if int(o[0])==0:
            link = subcat[1][t]
            # can't set incognito mode in all browsers, because
            # webbrowser.get().__dict__: {'args': ['%s'], 'basename': 'xdg-open', 'name': 'xdg-open'}
            # so this lines only work for chromium:
            ichrom = webbrowser.get('chromium')
            ichrom.remote_args.append('--incognito')
            ichrom.open_new_tab(link)
            return link
        else:
            url = subcat[0][t]
            tool = subcat[0][t].split('/')[-1].lower() # tool-name from gh.com/u/tool-name
            install_tool(url,tool)
            run_tool(tool)
            return tool
    except ValueError as e:
        if o=='x':
            print("bye!")
            sys.exit(0)
        elif o=='ls':
            print("installed tools:\033[1m")
            for f in os.listdir():
                if os.path.isdir(f) and f[0]!='.':
                    print(f)
            print("\033[0m",end="")
        else:
            print("invalid value")
    except IndexError:
        if o=='':
            print_index()
        else:
            print("invalid value")

def install_tool(url,tool):
    try:
        owd = os.getcwd()
        os.chdir(tool)
        os.chdir(owd) #change dir back
    except FileNotFoundError:
        subprocess.run(["git","clone",url+".git",tool]) #git clone "gh.com/the_tool.git" to the "tool" dir
        #TODO: if requeriments.txt: pip install -r requirements.txt

def run_tool(tool):
    owd = os.getcwd()
    os.chdir(tool)
    print("\033[1mlet's run <<%s>>! see you later!\n - tools.py\033[0m" %(tool))
    subprocess.run(["python3",tool+".py"])
    print("\033[1mhi again!\n - tools.py\033[0m")
    #TODO: read input and run python3 tool.py [input]
    os.chdir(owd) #change dir back

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
    while True:
        p = choosed_tool()
