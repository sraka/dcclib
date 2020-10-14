#!/usr/bin/env python
# coding=utf-8

print("Import Module : {}".format(__name__))
import pymel.core as pm
import maya.cmds as cmds


def list_all_node_types():
    """
    get all list of all DAG nodes types present in maya
    :return:
    """
    return cmds.ls(nt=True)











