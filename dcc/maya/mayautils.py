"""Utilities functions defined in this module to bebug/investigate diff maya file attributes
"""
__author__ = "sraka"
__email__ = ""
__module__ = "__{}__".format(__name__)
print(__module__)

import os
import sys

def get_env_sep():
    if sys.platform == "win32":
        return ";"
    else:
        return ":"

def get_env_var_paths(env, state='all'):
    """
    env : the env variable name you want to get the paths of
        MAYA_SCRIPT_PATH
        PYTHONPATH
        MAYA_PLUG_IN_PATH
    :param env:
    :return:
    :examples:
        get_env_paths("MAYA_SCRIPT_PATH")
        get_env_paths("MAYA_SCRIPT_PATH", state="default")
        get_env_paths("MAYA_SCRIPT_PATH", state="custom")
    """

    path_list = os.getenv(env).split(get_env_sep())

    # check for the entered state
    acceptable_states = ["all", "default", "custom"]
    if state not in acceptable_states:
        raise ValueError("The entered state |{}| is not acceptable , only |{}| states are acceptable".format(
            state, acceptable_states
        ))

    if sys.platform == 'win32':
        if state == "all":
            filtered = path_list
        if state == "default":
            filtered = [each for each in path_list if each.startswith("C:")]
        if state == "custom":
            filtered = [each for each in path_list if not each.startswith("C:")]
    else:
        raise OSError("Method not written for other operating systems")

    print('\n'.join(map(str, filtered)))

def list_env_variables(prefix="all"):
    """
    Collection of MAYA env variable with their descriptions
    :return:
    :examples:
        mayautils.list_env_variables(prefix="all") or mayautils.list_env_variables()
        mayautils.list_env_variables(prefix="MAYA")
        mayautils.list_env_variables(prefix="TAU")
    """
    all_env = os.environ
    if prefix == "all":
        for each in all_env:
            print(each)
    else:
        for each in all_env:
            if each.startswith(prefix):
                print(each)

