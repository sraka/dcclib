"""

"""

import os
import sys

from Qt import QtGui, QtCore, QtWidgets

app = QtWidgets.QApplication.instance()

class NukeGui(object):
    def __init__(self):
        print(__name__)

    @staticmethod
    def NukeWindow():
        for widget in app.topLevelWidgets():
            if widget.metaObject().className() == 'Foundry::UI::DockMainWindow':
                return widget

    @staticmethod
    def register_ui(func, title=None, panel=None):
        """
        Args :      func = Name of Function to be called (str)
                    title = title of the tool (str)
                    panel = Panel name (1 = Properties Panel , 2 = Viewer Panel)
        Example :   register_ui(func = 'NukeTestWindow')
                    register_ui(func = 'NukeTestWindow',title = 'TestWindow',panel=2)
        """
        if panel == 1 or panel == None:
            panel = 'Properties.1'
        elif panel == 2:
            panel = 'Viewer.1'

        if title == None:
            title = 'Test'

        pane = nuke.getPaneFor(str(panel))
        panels.registerWidgetAsPanel(str(func), str(title), 'uk.co.thefoundry.{}_UI'.format(title), True).addToPane(pane)
