import os
import sys
# from PySide import QtGui , QtCore
import maya.OpenMayaUI as OpenMayaUI
from shiboken import wrapInstance
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

maya_main_window_ptr = OpenMayaUI.MQtUtil.mainWindow()
maya_main_window = wrapInstance(long(maya_main_window_ptr),QtGui.QWidget)
maya_main_window_dock = wrapInstance(long(maya_main_window_ptr),QtGui.QMainWindow)



class MayaWindow(QtGui.QWidget):
    def __init__(self,tool_name):
        """  """
        self.tool_name = tool_name
        self.deleteInstances()
        super(MayaWindow,self).__init__(parent = maya_main_window)
        self.setObjectName(self.tool_name)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle(self.tool_name)
        self.setupUI()
        self.show()

    def setupUI(self):
        pass
    
    def deleteInstances(self):
        for obj in maya_main_window.children():
            if obj and obj.objectName() == self.tool_name:
                obj.setParent(None)
                obj.deleteLater()
                return
    
class MayaWindowDockable(MayaQWidgetDockableMixin , QtGui.QMainWindow):
    def __init__(self, tool_name, position=None):
        """  
            Args:
                tool_name = name of the tool
                position = right / left / top / bottom (str) . Define the position in __init__('UI','top') , bedefault it will bw docked on right side.
            Returns:
                    asasasa
            ex: 

        """
        self.tool_name = tool_name
        if not position:
            position = 'right'
        self.callbacks = []
        self.deleteInstances()
        super(MayaWindowDockable,self).__init__(parent = maya_main_window_dock)
        self.setObjectName(self.tool_name)
        self.setWindowFlags(QtCore.Qt.Window)
        self.setWindowTitle(self.tool_name)
        self.setupUI()
        self.show(dockable=True, floating = False , area = position)
        self.raise_()

    def setupUI(self):
        pass
    
    def dockCloseEventTriggered(self):
        self.deleteInstances()
    
    def removeCallbacks(self):
        for _callback in self.callbacks:
            print _callback , 'removing'
            OpenMaya.MSceneMessage.removeCallback(_callback)

    def addCallback(self, callback_type , func):
        _callback = OpenMaya.MSceneMessage.addCallback(callback_type, func)
        print _callback , 'adding'
        self.callbacks.append(_callback)
        
    def deleteInstances(self):
        for obj in maya_main_window_dock.children():
            if obj and 'widget' in dir(obj) and callable(obj.widget) and obj.widget() is not None and obj.widget().objectName() == self.tool_name : 
                self.removeCallbacks()
                maya_main_window_dock.removeDockWidget(obj)
                obj.setParent(None)
                obj.deleteLater()
                return

