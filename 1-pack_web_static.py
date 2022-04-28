#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
folder of AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    create the tgz archive
    """
    dateNow = datetime.now()
    archiveName = 'web_static_{}.tgz'.format(dateNow.strftime("%Y%m%d%H%M%S"))
    local('mkdir -p versions')
    local('tar -cvzf versions/{} web_static'.format(archiveName))
