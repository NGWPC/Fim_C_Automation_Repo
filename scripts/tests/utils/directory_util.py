import os
import logging
import shutil

def create_directory(directory):
    os.makedirs(os.path.expanduser(directory), exist_ok = True)
    assert os.path.exists(os.path.expanduser(directory))


def remove_directory(directory):
    if os.path.exists(os.path.expanduser(directory)):
       shutil.rmtree(os.path.expanduser(directory))
    assert not os.path.exists(os.path.expanduser(directory))
