#!/usr/bin/python

# Creates signature header for your LaTex files

import sys
import datetime
import traceback
import getpass
import getopt

if __name__ == '__main__':

    try:        
        author = getpass.getuser()
        optlist,args = getopt.getopt(sys.argv[1:],'a:e:f:')        
        src,email="",""
        for a,b in optlist:
            if a == '-f':
                src = b
            elif a == '-e':
                email = b 
            elif a == '-a':
                author = b
            elif a == 'h':
                exit()
        if not src:#file:
            exit() 
        if not ".tex" in src:
            src += ".tex" 

        # creates backup file
        f = open(src,"r")
        text = f.read()
        f.close()

        # find the start of LaTex document
        index = text.find('\\')
        f2 = open(src+"~","w")
        f2.write(text)
        f2.close()
        
        # write the data to the new file        
        f = open(src,"w")
        f.write("% author: {0}\n".format(author))
        if email:
            f.write("% mail: {0}\n".format(email))        
        f.write("% date: {0}\n".format(str(datetime.date.today().isoformat())))
        for i in args:
            f.write("% {0}\n".format(i))
        f.write("\n")
        index = 0 if index < 0 else index
        f.write(text[index:])
        f.close()
        # output to std what has been done
        print("The header containg signature was writen")
        print("in the file: {0}".format(src))
        print("(c) Tomas Trnka 2013")
    except:
        # inform about error and show hints
        print("You have to enter at least one parameter - the input file")
        print("Usage: -f specify source file")
        print("       -a set the author name other then system user name")
        print("       -e possible argument for email")
        print("       -h print this help")
        print("       everything without parameter will be outputed afterwards")
        print("       {0} [options -a-f-e] [optional args]".format(sys.argv[0]))
        #traceback.print_exc(file=sys.stdout)    
   
