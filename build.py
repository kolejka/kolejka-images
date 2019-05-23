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
            build_dir = os.path.join(PROJECT_PATH, repository, tag)
            dfile_path = os.path.join(build_dir, DFILE)
            try:
                build_tag = TEMPTAG+'/'+repository+':'+tag
                subprocess.run(['docker', 'build', os.path.dirname(dfile_path), '--tag', build_tag], check=True)
                for repo in repositories:
                    if repo == TEMPTAG:
                        continue
                    pub_tag = repo + '/'+repository+':'+tag
                    subprocess.run(['docker', 'rmi', pub_tag])
                    subprocess.run(['docker', 'tag', build_tag, pub_tag], check=True)
                    subprocess.run(['docker', 'push', pub_tag])
                if (TEMPTAG not in repositories) and (len(repositories) > 0):
                    subprocess.run(['docker', 'rmi', build_tag])
            except:
                traceback.print_exc()
                pass
