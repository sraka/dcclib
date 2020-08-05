"""
Functions for
"""
import nuke
import nukescripts

def listVrayNodes():
    """
    Get the list of all vray nodes present in the nuke scene.
    :return:
    """
    return [node.name() for node in nuke.allNodes() if 'VRay' in node.Class()]
