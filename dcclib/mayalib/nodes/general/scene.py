"""
get
list
set
remove/delete
"""

print("Import Module : {}".format(__name__))
import pymel.core as pm
import maya.cmds as cmds

def get_scene_name():
    return pm.sceneName().namebase.__str__()

def get_scene_path():
    return pm.sceneName().abspath().__str__()

def get_scene_dir():
    return pm.sceneName().dirname().__str__()

def get_workspace_path():
    return str(pm.Workspace().path.dirname())

def delete_unknown_nodes():
    """
    Delete all the unknown nodes present in the scene file
    :return:
    """
    print("Deleting Unknown Nodes")
    cmds.delete(cmds.ls(type='unknown'))

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

def list_all_plugins(status="all", info=False):
    """
    List all plugins , with details
    :param status:
    :param info: list the info as well (version,path installed)
    :return:
    """
    if status == "enabled":
        print("all active plugins")
    elif status == "disabled":
        print("all inactive plugins")
    elif status == "all":
        print("List all plugins")

print("Improrted Scene module   END. {}".format(__name__))
