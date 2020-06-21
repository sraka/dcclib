"""

SUGGESTED USAGE IN PYTHON SCRIPTS
from dcclib.nukelib import NukeLib
nukelib = NukeLib()
nukelib.nukescene.list_selected_nodes()


SUGGESTED USAGE WHILE LAUNCHING NUKE
This way of usage is suggested to be used while launching nuke(init.py),
so that it would be available inside nuke script editor on the go for quicker usage.

from dcclib.nukelib import NukeLib
nukegui = Nukelib().nukegui
nukenode = Nukelib().nukenode
nukescene = Nukelib().nukescene
nukevray = Nukelib().nukevray

"""

from dcclib.nukelib.nodes.gui import NukeGui
from dcclib.nukelib.nodes.node import NukeNode
from dcclib.nukelib.nodes.scene import NukeScene
from dcclib.nukelib.nodes.vray import NukeVray

__all__ = ['NukeLib', 'nodes']
required_modules = ['nuke', 'nukescripts']

class NukeLib(object):
    """
    from nukelib
    """
    def __init__(self):
        self.nukegui = NukeGui()
        self.nukenode = NukeNode()
        self.nukescene = NukeScene()
        self.nukevray = NukeVray()

    @staticmethod
    def test():
        print("Nuke Lib Post Method")
