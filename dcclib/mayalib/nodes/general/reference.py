import os
import sys
import pymel.core as pm
import maya.cmds as cmds


class MayaReference():
    def __init__(self):
        pass

    def get_refs_list_loaded(self,mode=None):
        if mode == 'list':
            return [ref.namespace for ref in pm.listReferences() if ref.isLoaded()]
        else:
            return [ref for ref in pm.listReferences() if ref.isLoaded()]

    def get_refs_list_unloaded(self,mode=None):
        if mode == 'list':
            return [ref.namespace for ref in pm.listReferences() if not ref.isLoaded()]
        else:
            return [ref for ref in pm.listReferences() if not ref.isLoaded()]

    def get_refs_list_nested(self):
        pass


