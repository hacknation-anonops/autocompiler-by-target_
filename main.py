#!/usr/bin/python
import os
import sys

version="2.1.1"

if os.geteuid() != 0: # check if we run as root
    print "This software must be run as root. Please try again with sudo."
    exit()

print "Auto crosscompiler by target_"
print "Version: "+version+"\n"

try: # handle extra args
    extra=" ".join(sys.argv[3:])
except:
    extra=""

arches=["mips","mipsel","powerpc","sh4","m68k","armv4l"] #dont fuck with these!

if len(sys.argv) < 2:
    print "Usage: "+sys.argv[0]+" <program.c> <path> <extra options(ex: -pthread)>"
    exit()

def setup(): #setup the compilers
    setup=raw_input("Setup crosscompilers?\n(yes/no): ")
	
    if setup == "yes":
        os.system("mkdir /etc/xcompile")
	for arch in arches:
	    os.system("wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-"+arch+".tar.bz2 -P /etc/xcompile/")
            os.system("tar -jxf /etc/xcompile/cross-compiler-"+arch+".tar.bz2 -C /etc/xcompile/")
	    os.system("mv /etc/xcompile/cross-compiler-"+arch+" /etc/xcompile/"+arch)
	os.system("rm /etc/xcompile/*.tar.bz2")

def main():
    setup()
    for arch in arches: 
        os.system("/etc/xcompile/"+arch+"/bin/"+arch+"-gcc "+sys.argv[1]+" "+extra+" -o "+sys.argv[2]+"-"+arch) #compile da shit

if __name__ == "__main__":
    main()
