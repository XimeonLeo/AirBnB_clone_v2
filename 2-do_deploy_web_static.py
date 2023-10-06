#!/usr/bin/python3
""" A module that creates an .tgz archive from the content of
        web_static
"""
from datetime import datetime
from fabric.api import local, task, run, put, env
import os

env.hosts[54.162.80.16, 54.236.45.116]


@task
def do_pack():
    """ A method that creates the archive """
    time = datetime.now()
    dt = "{}{}{}{}{}{}".format(time.year,
                               time.month,
                               time.day,
                               time.hour,
                               time.minute,
                               time.second)
    path = "versions/web_static_{}".format(dt)
    print("Packing web_static to {}".format(path))

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -czvf {} web_static".format(path)).failed is True:
        return None
    return path


@task
def do_deploy(archive_path):
    """ Destribute an archive to my web servers
    """
    try:
        if not os.path.exists(archive_path):
            return False
        zip_file = os.path.basename(archive_path)
        file = zip_file.split(".")[0]

        # putting the archive file in /tmp/ directory
        put(archive_path, "/tmp/")

        location = "/data/web_static/releases/"
        # replacing old file
        run("rm -rf {}{}".format(location, file))
        run("mkdir -p {}{}".format(location, file))

        # Uncompresaing archive file
        run("tar -xzf /tmp/{} -C {}{}".format(zip_file, location, file))

        # removing archive from the server('/tmp/')
        run("rm -rf /tmp/{}".format(zip_file))

        # recreating smylink
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(location, file))
        print('New version deployed!')
        return True

    except Exception:
        retuen False
