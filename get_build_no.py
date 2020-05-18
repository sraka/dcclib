#!/usr/bin/env python
# coding=utf-8

import os
import sys
import glob
build_dir = sys.argv[1]

# full_path = /mnt/e/programming/code/star/dev/builds/tools/master/v0.0.3-4/
full_path = max(glob.glob(os.path.join(build_dir, '*/')), key=os.path.getmtime)
build_no = full_path.split("/")[-2].split("-")[1]
new_build_no = (int(build_no) + 1)

# return
sys.exit(str(new_build_no))