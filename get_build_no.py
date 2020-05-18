#!/usr/bin/env python
# coding=utf-8

import os
import sys
import glob
build_dir = sys.argv[1]

# For a fresh module , if the build dir is not there , then create it
if not os.path.exists(build_dir):
    os.makedirs(build_dir)
    sys.exit(str(1))
else:
    # full_path = /mnt/e/programming/code/star/dev/builds/tools/master/v0.0.3-4/
    full_path = max(glob.glob(os.path.join(build_dir, '*/')), key=os.path.getmtime)
    build_no = full_path.split("/")[-2].split("-")[1]
    new_build_no = (int(build_no) + 1)

    # return
    sys.exit(str(new_build_no))