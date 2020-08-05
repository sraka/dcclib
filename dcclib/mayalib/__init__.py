"""

"""
__version__ = '0.0.1'
__author__ = 'sraka'

import pymel.core as pm
import maya.cmds as cmds
print("improted maya modules")

# from dcclib.mayalib.nodes.scene import MayaScene
import dcclib.mayalib.nodes.scene as ms
# __all__ = ['MayaLib', 'MayaScene', 'scene']
required_modules = ['pymel.core as pm', 'maya.cmds as cmds', 'maya.mel as mel']

class MayaLib(object):
    def __init__(self):
        self.mayascene = ms.MayaScene()

    @staticmethod
    def test():
        print("MayaLib test")

MayaLib()