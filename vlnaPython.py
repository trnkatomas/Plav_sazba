#!/usr/bin/python
# -*- coding: utf-8 -*-

# Adds nonbreakable spaces to your LaTex files

import sys
import datetime
import traceback
import getpass
import getopt
import re

if __name__ == '__main__':

    try:        
        author = getpass.getuser()
        optlist,args = getopt.getopt(sys.argv[1:],'f:b:a:')        
        src,email="",""
        infront_symbols = ["–"]
        afterwards_symbols = ["KkSsVvZzOoUuAIai"]

        for a,b in optlist:
            if a == '-f':
                src = b
            elif a == '-b':
                new_infront_symbols = b.split(",")
            elif a == '-a':
                new_afterwards_symbols = b.split(",")
            elif a == '-h':
                exit()
        if not src:#file:
            exit() 
        if not ".tex" in src:
            src += ".tex" 

        # creates backup copy of a file
        f = open(src,"r")
        text = f.read()
        f.close()
        f2 = open(src+"~","w")
        f2.write(text)
        f2.close()
        
        # creates new file with replacements
        replaced = 0   
        f = open(src,"w")   
        for symbol in infront_symbols:
            pattern = re.compile('\s+{}'.format(symbol))
            subst = "~{}".format(symbol)
            replaced += len(re.findall(pattern,text))
            text = re.sub(pattern, subst, text)

        for symbol in afterwards_symbols:
            pattern = re.compile('\s{}\s+'.format(symbol))
            subst = " {}~".format(symbol)
            replaced += len(re.findall(pattern,text))
            text = re.sub(pattern, subst, text)

        # months
        p = re.compile(r'(\d+\.)\s+(l[e|i][s|d]|čer|[p|s]r[o|p]|úno|břez|dub|kvě|zá|říj)(.*)?([r|n]a|ce|ří|du)\b')
        #p = re.compile(r'(\d+\.)\s+([a-z])')
        replaced += len(re.findall(p,text))
        subst = r"\1~\2\3\4"
        text = re.sub(p,subst, text)

        # born * year substitution
        p = re.compile(r'(\*)(\s)(\d{4})')
        replaced += len(re.findall(p,text))
        subst = r"\1\\,\3"
        text = re.sub(p,subst, text)        
    
        f.write(text)
        f.close()
        # output to std what has been done
        print("Chars replaced: {}".format(replaced))
        print("in the file: {0}".format(src))
        print("(c) Tomas Trnka 2015")
    except:
        # signal error and show hints
        print("You have to enter at least one parameter - the input file")
        print("Usage: -f specify source file")
        print("       -a symbols where ~ should be afterwards separated by comas x,x,x,x")
        print("       -b symbols where ~ should be before separated by comas x,x,x,x")
        print("       -h print this help")
        print("       {0} [options -f] [optional args]".format(sys.argv[0]))
        #traceback.print_exc(file=sys.stdout)
