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
    file_name = "web_static_{}{}{}{}{}{}".format(time.year,
                                                 time.month,
                                                 time.day,
                                                 time.hour,
                                                 time.minute,
                                                 time.second)

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed is True:
            return None

    if local(f"tar -czvf {file_name} web_static").failed is True:
        return None
    return file
