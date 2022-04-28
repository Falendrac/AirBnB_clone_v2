#!/usr/bin/python3
'''
script that generates a .tgz archive from the contents of the web_static
folder of AirBnB Clone repo, using the function do_pack.
'''

from fabric.api import local, run, put
from datetime import datetime


def do_pack():
    '''
    create the tgz archive
    '''
    dateNow = datetime.now()
    archiveName = f'web_static_{dateNow.strftime("%Y%m%d%H%M%S")}.tgz'
    local('mkdir -p versions')
    local(f'tar -zcvf versions/{archiveName} web_static')
