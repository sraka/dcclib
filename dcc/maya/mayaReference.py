import os
import sys
import pymel.core as pm
import maya.cmds as cmds

def get_loaded_refs_list(mode=None):
    if mode == 'list':
        return [ref.namespace for ref in pm.listReferences() if ref.isLoaded()]
    else:
        return [ref for ref in pm.listReferences() if ref.isLoaded()]

def get_unloaded_refs_list(mode=None):
    if mode == 'list':
        return [ref.namespace for ref in pm.listReferences() if not ref.isLoaded()]
    else:
        return [ref for ref in pm.listReferences() if not ref.isLoaded()]

def get_nested_refs_list():
    pass


