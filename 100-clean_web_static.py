#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import *
import os


env.user = 'ubuntu'
env.hosts = ['54.172.179.45', '100.26.167.148']


def do_clean(number=0):
    """Deletes out-of-date archives in versions and releases folders."""
    try:
        number = int(number)
        if number < 0:
            return
        number = 1 if number == 0 else number + 1

        # Clean local versions folder
        with lcd("versions"):
            local("ls -t | tail -n +{} "
                  "| xargs -I {{}} rm -- {{}}".format(number))

        # Clean remote versions folder on both servers
        with cd("/data/web_static/releases"):
            run("ls -t | tail -n +{} | xargs -I {{}} "
                "rm -rf -- {{}}".format(number))

    except Exception as e:
        print("Clean failed:", str(e))


if __name__ == "__main__":
    do_clean()
