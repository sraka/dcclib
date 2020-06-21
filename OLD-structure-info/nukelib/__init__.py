"""

"""
__version__ = '0.0.1'
__author__ = 'sraka'

from nukelib.NukeSession import NukeSession
from nukelib.NukeVray import NukeVray

class NukeLib(object):
    def __init__(self):
        self.nukescene = NukeSession()
        self.nukevray = NukeVray()

    @staticmethod
    def post():
        print("Nuke Lib Post Method")


