# NUKE

## Registering PySide UI's

Example UI
``` python
from PySide2 import QtGui, QtWidgets

class Boilerplate(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Boilerplate, self).__init__()
        
        main_l = QtWidgets.QVBoxLayout()
        self.setLayout(main_l)
        self.button_1 = QtWidgets.QPushButton("Button_1")
        main_l.addWidget(self.button_1)

        self.show()

# window = Boilerplate()
```

Registering this ui using Nuke Native Method
``` python
pane = nuke.getPaneFor("Properties.1")
panel = nukescripts.panels.registerWidgetAsPanel('Boilerplate', 'Test panel', 'uk.co.thefoundry.Boilerplate', True)
panel.addToPane(pane)
```

Registering using nukelib
``` python
import dcclib.nukelib as nl
nl.gui.registerUiPySide("Boilerplate")                  # By default it registers on Properties panel
```
Other examples
``` python
nl.gui.registerUiPySide("Boilerplate", panel="Viewer")                          # To register on viewer panel
nl.gui.registerUiPySide("Boilerplate", panel="Viewer", title="MyNewWidow")      # Input window name 
```
