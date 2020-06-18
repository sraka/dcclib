#!/usr/bin/env python
# coding=utf-8

import sys
# sys.path.append(r"E:\development\acgfilms\repos\snips-py\test\api\slack\pythonModules\slacker\venv\lib\python2.7\site-packages")
# from slacker import Slacker
sys.path.append(r"E:\development\acgfilms\repos\FRAMEWORKS\corelib\dcc")
from nukelib import NukeLib

nukelib = NukeLib()
nukelib.nukescene.test()
# nukelib.nukevray.test()

# nukescene = NukeLib().nukescene
# nukescene.test()
# nukevray = NukeLib().nukevray
# nukevray.test()