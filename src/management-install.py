#!/usr/bin/env python2

import sys
import os
import platform
import fileinput
from helper import Helper
helper = Helper()

def main():
    helper.is_root()
    helper.prepare()
    install_management()

def install_management():
    if (platform.dist()[0] == 'centos'):
        os.system('yum install -y beegfs-mgmtd')
    elif (platform.dist()[0] == 'Ubuntu'):
        os.system('apt-get install -y beegfs-mgmtd')
    else:
        print('Operating system not supported')
        sys.exit('Exiting installer')
    os.system('''
    /opt/beegfs/sbin/beegfs-setup-mgmtd -p /data/beegfs/beegfs-mgmtd
    /etc/init.d/beegfs-mgmtd start
    /etc/init.d/beegfs-mgmtd status
    ''')

main()
