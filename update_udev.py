#!/usr/bin/env python2

import subprocess
import os

os.putenv('ANSIBLE_HOST_KEY_CHECKING', 'False')

subprocess.call([
    'ansible-playbook',
    '--inventory-file=inventory.ini',
    'update_udev.yml'
])
