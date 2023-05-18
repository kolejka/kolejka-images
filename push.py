#!/usr/bin/env python3
# vim:ts=4:sts=4:sw=4:expandtab

import os
import re
import subprocess
import traceback

IMAGES_SPEC='IMAGES'
REPOSITORIES_SPEC='REPOSITORIES'
PROJECT_PATH=os.path.dirname(__file__)
IMAGES_PATH=os.path.join(PROJECT_PATH, IMAGES_SPEC)
REPOSITORIES_PATH=os.path.join(PROJECT_PATH, REPOSITORIES_SPEC)
DFILE='Dockerfile'
TEMPTAG='kolejkatemp'

repositories=[]
with open(REPOSITORIES_PATH) as repositories_file:
    for line in repositories_file.readlines():
        line = line.strip()
        if line.startswith('#'):
            continue
        repositories.append(line)

with open(IMAGES_PATH) as images_file:
    for line in images_file.readlines():
        line = line.strip()
        if line.startswith('#'):
            continue
        m = re.match(r'([a-z]+):([a-z.0-9]+)', line)
        if m:
            repository = m.group(1)
            tag = m.group(2)
            for repo in repositories:
                try:
                    if repo == TEMPTAG:
                        continue
                    pub_tag = repo + '/'+repository+':'+tag
                    subprocess.run(['docker', 'push', pub_tag])
                except:
                    traceback.print_exc()
                    pass
