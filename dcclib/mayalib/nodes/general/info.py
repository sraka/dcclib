#!/usr/bin/env python
# coding=utf-8

import maya.cmds as cmds
import pymel.core as pm

def test():
    print("Maya Info")

def get_maya_version():
    pass

def get_maya_version():
    return cmds.about(version=True)

def get_maya_api_version():
    return int(cmds.about(api=True))



