#!/usr/bin/python

import os
import sys
from shutil import copyfile

if len(sys.argv) < 2:
    print "Please use: python "+sys.argv[0]+" install/uninstall"
    exit()

if os.geteuid() != 0: # check if we run as root
    print "This software must be run as root. Please try again with sudo."
    exit()

else:
    if sys.argv[1] == "install":
        copyfile("main.py", "/usr/bin/autocompile")
        os.chmod("/usr/bin/autocompile", 0775)
        print "Installed succesfully! Type 'autocompile' now!"

    elif sys.argv[1] == "uninstall":
        os.remove("/usr/bin/autocompile")
        print "Uninstall completed"

    else:
        print "Please use: python "+sys.argv[0]+" install/uninstall"
