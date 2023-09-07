#!/usr/bin/python3
"""
This Fabric script that deploys an archive to web servers.
"""

from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['54.172.179.45', '100.26.167.148']


def do_deploy(archive_path):
    """
    Deploys a web_static archive to the web servers.
    Returns True if successful, False otherwise.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]
        remote_archive = "/tmp/{}".format(archive_filename)

        # Upload archive to the /tmp/ directory on the web server
        put(archive_path, remote_archive)

        # Create the release directory
        run("mkdir -p /data/web_static/releases/{}/".format(archive_no_ext))

        # Uncompress the archive to the release directory
        run("tar -xzf {} -C /data/web_static/releases/{}/".format(
            remote_archive, archive_no_ext))

        # Delete the uploaded archive from the web server
        run("rm {}".format(remote_archive))

        # Move the contents to the appropriate directory
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                archive_no_ext, archive_no_ext))

        # Remove the web_static directory from the release directory
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_no_ext))

        # Remove the existing symbolic link if it exists
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(archive_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        print("Deployment failed:", str(e))
        return False
