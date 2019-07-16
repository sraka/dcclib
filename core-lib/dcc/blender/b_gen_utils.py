import os
import bpy


class Gen_Utils(object):

    def __init__(self):
        pass

    @staticmethod
    def get_blender_version():
        """
        Gives the current blender version.
        :return: A `str` formatted like: "2.79.0"
        """
        return ".".join([str(i) for i in bpy.app.version])