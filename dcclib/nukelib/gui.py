"""
Functions related to nuke GUI
"""

import os
import sys
import nuke
import nukescripts
from PySide2 import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication.instance()
def test_():
    print("test")

def list_nuke_menus():
    return [e.name() for e in nuke.menu('Nuke').items()]

def list_node_menus():
    return [e.name() for e in nuke.menu('Nodes').items()]

def NukeWindow():
    for widget in app.topLevelWidgets():
        if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
            return widget

def registerUiPySide(func, title=None, panel=None):
    """
    Register the UI as a panel
    Args :      func = Name of Function to be called (str)
                title = title of the tool (str)
                panel = Panel name (default='Properties', 'Viewer')

    Example :   nl.gui.registerUiPySide("Boilerplate")
                nl.gui.registerUiPySide("Boilerplate", panel="Viewer")
                nl.gui.registerUiPySide("Boilerplate", panel="Viewer", title="MyNewWidow")
    :param func: str
    :param title: str
    :param panel:
    :return:
    """
    if panel == 'Properties' or panel == None:
        panel = 'Properties.1'
    elif panel == 'Viewer':
        panel = 'Viewer.1'

    if title == None:
        title = '{}_UI'.format(func)

    pane = nuke.getPaneFor(str(panel))
    pane_ui = nukescripts.panels.registerWidgetAsPanel(str(func), str(title), 'uk.co.thefoundry.{}_pane'.format(title), True)
    pane_ui.addToPane(pane)
