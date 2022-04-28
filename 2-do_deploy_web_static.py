#!/usr/bin/python3
'''
script (based on the file 1-pack_web_static.py) that distributes
an archive to web servers, using the function do_deploy
'''

from fabric.api import run, put, env
from os.path import exists

env.hosts = ['35.196.116.56', '35.237.116.242']


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
