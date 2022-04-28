#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
folder of AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local, run, put, env
from datetime import datetime
from os.path import exists

env.hosts = ['35.196.116.56', '35.237.116.242']


def do_pack():
    """
    create the tgz archive
    """
    try:
        dateNow = datetime.now()
        archiveName = 'web_static_{}.tgz'.format(dateNow.strftime(
            "%Y%m%d%H%M%S"))
        local('mkdir -p versions')
        local('tar -cvzf versions/{} web_static'.format(archiveName))
        return "versions/{}".format(archiveName)
    except Exception:
        return None


def do_deploy(archive_path):
    '''
    deploy the archive in the web server
    '''
    if not exists(archive_path):
        return False

    try:
        archiveSplit = archive_path.split("/")
        archiveName = archiveSplit[1]
        filename = archiveName.split(".")[0]
        releasePath = "/data/web_static/releases/"

        put(archive_path, "/tmp/{}".format(archiveName))

        run("mkdir -p {}/{}/".format(releasePath, filename))
        run("tar -xzf /tmp/{} -C {}/{}/".format(archiveName, releasePath,
            filename))

        run("rm /tmp/{}".format(archiveName))

        run("mv {}/{}/web_static/* {}/{}/".format(releasePath, filename,
            releasePath, filename))
        run("rm -rf {}/{}/web_static".format(releasePath, filename))

        run("rm -rf /data/web_static/current")
        run("ln -s {}/{}/ /data/web_static/current".format(releasePath,
            filename))

        print("New version deployed!")

        return True
    except Exception:
        return False


def deploy():
    '''
    creates and distributes an archive to web servers
    '''
    archiveIsCreate = do_pack()
    if archiveIsCreate is None:
        return False
    return do_deploy(archiveIsCreate)
