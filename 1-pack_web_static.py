#!/usr/bin/python3
""" A module that creates an .tgz archive from the content of
        web_static
"""
from datetime import datetime
from fabric.api import local, task
import os


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
