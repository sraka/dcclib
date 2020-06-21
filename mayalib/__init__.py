"""

"""
__version__ = '0.0.1'
__author__ = 'sraka'

from dcclib.mayalib.nodes.scene import MayaScene

# __all__ = ['MayaLib', 'MayaScene', 'scene']
required_modules = ['pymel.core as pm', 'maya.cmds as cmds', 'maya.mel as mel']

class MayaLib(object):
    def __init__(self):
        self.mayascene = MayaScene()

    @staticmethod
    def test():
        print("MayaLib test")