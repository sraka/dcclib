"""

SUGGESTED USAGE IN PYTHON SCRIPTS
from dcclib.nukelib import NukeLib
nukelib = NukeLib()
nukelib.nukescene.list_selected_nodes()


SUGGESTED USAGE WHILE LAUNCHING NUKE
This way of usage is suggested to be used while launching nuke(init.py),
so that it would be available inside nuke script editor on the go for quicker usage.
"""
import node
import scene
import vray
import gui

import nuke
import nukescripts

