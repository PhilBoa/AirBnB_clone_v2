#!/usr/bin/python3
"""
This Fabric script defines a function to create a compressed .tgz archive
of the web_static folder. It also follows specific naming conventions for the
archive and stores it in the versions folder.

Usage:
    fab -f 1-pack_web_static.py do_pack
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Create a compressed .tgz archive of the web_static folder.
    Returns the path to the created archive or None if it fails.
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(archive_name))

    if result.succeeded:
        return archive_name
    else:
        return None
