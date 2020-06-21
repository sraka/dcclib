import os 
import sys
import maya.cmds as cmds
import pymel.core as pm

def intr_add_modifier(description_name, node_type, node_label):
    """ 
        Des:
            It adds a "modifier node" for the given xgen description. 
        Args:
            description_name(str) = 
            node_type(str) = NodeType Name eg: 'xgmModifierNoise'
            node_label(str) = Name/label of the node
        
    """
    description_node_inPlug = '{}_Shape.inSplineData'.format(description_name)
    description_node = pm.PyNode(description_node_inPlug)
    cur_in = description_node.listConnections(p=1)
    modifier = pm.createNode(node_type, n=node_label)
    modifier_inPlug = modifier + r'.inSplineData'
    modifier_outPlug = modifier + r'.outSplineData'
    pm.connectAttr(modifier_outPlug,description_node_inPlug,f=1)
    pm.connectAttr(cur_in[0],modifier_inPlug)








