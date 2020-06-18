"""

"""

__module__ = "__{}__".format(__name__)

import os
import sys
# import pymel.core as pm
# import maya.cmds as cmds

class MayaScene(object):
    def __init__(self):
        print(__name__)

    @staticmethod
    def get_scene_name():
        return pm.sceneName().namebase.__str__()

    @staticmethod
    def get_scene_path():
        return pm.sceneName().abspath().__str__()

    @staticmethod
    def get_scene_dir():
        return pm.sceneName().dirname().__str__()

    @staticmethod
    def get_workspace_path():
        return str(pm.Workspace().path.dirname())

    @staticmethod
    def delete_unknown_nodes():
        """
        Delete all the unknown nodes present in the scene file
        :return:
        """
        print("Deleting Unknown Nodes")
        cmds.delete(cmds.ls(type='unknown'))

    @staticmethod
    def delete_unknown_plugins():
        """
        Delete all the unknown plugins present in the scene file
        :return:
        """
        plugins_list = cmds.unknownPlugin(q=True, l=True)
        if plugins_list:
            for plugin in plugins_list:
                print(plugin)
                cmds.unknownPlugin(plugin, r=True)

    @staticmethod
    def list_all_plugins(status=all, info=False):
        """
        List all plugins , with details
        :param status:
        :param info: list the info as well (version,path installed)
        :return:
        """
        if status == "enabled":
            print("all active plugins")
        if status == "disabled":
            print("all inactive plugins")
        if status == "all":
            print("List all plugins")
