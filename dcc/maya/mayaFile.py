import os
import sys
import pymel.core as pm
import maya.cmds as cmds


def get_scene_name():
    return pm.sceneName().namebase.__str__()

def get_scene_path():
    return pm.sceneName().abspath().__str__()

def get_scene_dir():
    return pm.sceneName().dirname().__str__()

def get_workspace_path():
    return str(pm.Workspace().path.dirname())

