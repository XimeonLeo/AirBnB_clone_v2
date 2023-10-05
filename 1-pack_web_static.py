#!/usr/bin/python3
""" A module that creates an .tgz archive from the content of
        web_static
"""
from datetime import datetime
from fabric.api import local
import os


def do_pack():
    """ A method that creates the archive """
    time = datetime.utcnow()
    file_name = "versions/web_static_{}{}{}{}{}{}".format(time.year,
                                                          time.month,
                                                          time.day,
                                                          time.hour,
                                                          time.minute,
                                                          time.second)

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -czvf {} web_static".format(file_name)).failed is True:
        return None
    return file_name
