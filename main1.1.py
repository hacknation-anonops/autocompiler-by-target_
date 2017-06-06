#!/usr/bin/python
import os
import sys
if os.geteuid() != 0:
    print "This software must be run as root. Please try again with sudo."
    sys.exit(0)
print "Auto crosscompiler by target_\n"
try:
    extra=sys.argv[3]
except:
    extra=""
arches=["mips","mipsel","powerpc","sh4","m68k","armv4l"]
def help():
    print "Usage: "+sys.argv[0]+" <program.c> <output-name> <extra options(ex: -pthread)>"
if len(sys.argv) < 2:
    help()
    exit(1)
x=raw_input("Setup crosscompilers?\n(yes/no): ")
def run():
    paths()
    os.system("source /root/.bashrc")
    for arch in arches: 
        os.system(arch+"-gcc "+sys.argv[1]+" "+extra+" -o "+sys.argv[2]+"-"+arch)
def paths():
    found=False
    f=open("/root/.bashrc", "a+")
    if """export PATH=$PATH:/etc/xcompile/armv4l/bin
export PATH=$PATH:/etc/xcompile/armv6l/bin
export PATH=$PATH:/etc/xcompile/i586/bin
export PATH=$PATH:/etc/xcompile/m68k/bin
export PATH=$PATH:/etc/xcompile/mips/bin
export PATH=$PATH:/etc/xcompile/mipsel/bin
export PATH=$PATH:/etc/xcompile/powerpc/bin
export PATH=$PATH:/etc/xcompile/powerpc-440fp/bin
export PATH=$PATH:/etc/xcompile/sh4/bin
export PATH=$PATH:/etc/xcompile/sparc/bin
export PATH=$PATH:/etc/xcompile/armv6l/bin""" in f.read():
	found=True
        if found != True:
   	    f.write("""export PATH=$PATH:/etc/xcompile/armv4l/bin
export PATH=$PATH:/etc/xcompile/armv6l/bin
export PATH=$PATH:/etc/xcompile/i586/bin
export PATH=$PATH:/etc/xcompile/m68k/bin
export PATH=$PATH:/etc/xcompile/mips/bin
export PATH=$PATH:/etc/xcompile/mipsel/bin
export PATH=$PATH:/etc/xcompile/powerpc/bin
export PATH=$PATH:/etc/xcompile/powerpc-440fp/bin
export PATH=$PATH:/etc/xcompile/sh4/bin
export PATH=$PATH:/etc/xcompile/sparc/bin
export PATH=$PATH:/etc/xcompile/armv6l/bin""")
            f.close()
if x == "yes":
    os.system("mkdir /etc/xcompile")
    os.system("""cd /etc/xcompile;
    wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-armv4l.tar.bz2;
    wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-i586.tar.bz2;
 wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-m68k.tar.bz2;
 wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mips.tar.bz2;
 wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-mipsel.tar.bz2;
 wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-powerpc.tar.bz2;
 wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sh4.tar.bz2;
 wget https://www.uclibc.org/downloads/binaries/0.9.30.1/cross-compiler-sparc.tar.bz2;
 wget http://distro.ibiblio.org/slitaz/sources/packages/c/cross-compiler-armv6l.tar.bz2;
 tar -jxf cross-compiler-armv4l.tar.bz2;
 tar -jxf cross-compiler-i586.tar.bz2;
 tar -jxf cross-compiler-m68k.tar.bz2;
 tar -jxf cross-compiler-mips.tar.bz2;
 tar -jxf cross-compiler-mipsel.tar.bz2;
 tar -jxf cross-compiler-powerpc.tar.bz2;
 tar -jxf cross-compiler-sh4.tar.bz2;
 tar -jxf cross-compiler-sparc.tar.bz2;
 tar -jxf cross-compiler-armv6l.tar.bz2;
 rm *.tar.bz2;
 mv cross-compiler-armv4l armv4l;
 mv cross-compiler-i586 i586;
 mv cross-compiler-m68k m68k;
 mv cross-compiler-mips mips;
 mv cross-compiler-mipsel mipsel;
 mv cross-compiler-powerpc powerpc;
 mv cross-compiler-sh4 sh4;
 mv cross-compiler-sparc sparc;
 mv cross-compiler-armv6l armv6l""")
run()


