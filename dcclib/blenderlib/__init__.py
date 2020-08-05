#!/usr/bin/env python
# coding=utf-8

__version__ = '0.0.1'
__author__ = 'sraka'

from dcclib.blenderlib.nodes.info import BlenderInfo

required_modules = ['bpy']

class BlenderLib(object):
    """
    from blenderlib
    """
    def __init__(self):
        self.blenderinfo = BlenderInfo()

    @staticmethod
    def test():
        print("Nuke Lib Post Method")
