"""

"""

from dcclib.mayalib.nodes.general import scene

# TODO :
# Loading all functions in __init__ so that they are available instantly ,
# eg : ml.list_all_plugins() instead of ml.scene.list_all_plugins()
# This is loading fine, but the method is not visible in autocomplete, fix this later
# The method should be visible in autocomplete. similar to pm module
# from dcclib.mayalib.nodes.general.scene import *


import pymel.core as pm
import maya.cmds as cmds

print("SDFSDF")

def _modules(module, all=None):
    """
    Method to list all the mayalib modules imported.
    examples:
    ml._modules(ml)             # List custom dcclib.mayalib modules
    ml._modules(ml, all=True)   # List all modules in dcclib.mayalib
    :param module:
    :param all:
    :return:
    """
    import inspect

    # mod_list = [('cmds', <module 'maya.cmds' from
    # 'C:\Program Files\Autodesk\Maya2018\Python\lib\site-packages\maya\cmds\__init__.py'>)]
    mod_list = inspect.getmembers(module, inspect.ismodule)

    ignore_methods = ['cmds', 'pm', 'nodes']

    for eachmod in mod_list:
        if eachmod[0] not in ignore_methods and all is None:
            print('{module_name} -> {module_path}'.format(
                module_name=eachmod[0],
                module_path=eachmod[1]
            ))
        elif all is True:
            print('{module_name} -> {module_path}'.format(
                module_name=eachmod[0],
                module_path=eachmod[1]
            ))


print("asdfsfsfa--")
