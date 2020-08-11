# dcclib

This is a library of python scripts which are used by pipeline TD's or
Dept TD's regularly.

## Project Goals
This project was created with a goal to have a custom lib for dcc packages
which are being used in a studio and have regularly used functions written
in a common dir for ease of access.

## Who is dcclib for?

**For Novice**

**For Technical Director**
There are many instances where TD's write maya scripts , these methods  
can be used to quickly get some jobs done without writing the same lines  
over and over again in every maya python script.

**For Techhical TroubleShooting**
Methods from these can be used for quick trouble shooting of the scene  
file in your dcc package.  
Makes the process of finding the problem faster.

## Installation

## Quick Start | Getting Started

examples:
Use in Python Scripts / DCC script editor
``` python
import dcclib.mayalib as ml
import dcclib.nukelib as nl
import dcclib.blenderlib as bl
```
Usage inside the DCC appliacation.

Setup before launch  (Describe this later)  
NUKE:  
    add in nuke.pluginAddPath() in __init__ file  
MAYA :  
    add in PYTHONPATH ??

After launching your dcc application.
    Add the path where your dcclib module is present in sys.path


#### NUKE
Place these inside the init.py file of nuke.
``` python
import dcclib.nukelib as nl

# MODULE : scene
nl.scene.delete_all_nodes()
nl.scene.deselect_all_nodes()
help(nl.scene.list_disabled_nodes)

# MODULE : node
selNode = nuke.selectedNode()
nl.node.isEnabled(selNode)
nl.node.isUsingLifetime(selNode)
nl.node.getAllInputs(selNode)
nl.node.__name__   # Module name : 'dcclib.nukelib.node'
nl.node.__doc__    # Module docstring
nl.node.__file__   # Module File path 
nl.node.__class__  # <type 'module'>

# MODULE : gui
nl.gui.NukeWindow()
nl.gui.list_node_menus()
nl.gui.list_nuke_menus()
nl.gui.registerUi()

# MODULE : vray
nl.vray.list_vray_nodes()

```

#### MAYA
Place this inside the userSetup.py file of maya.
``` python
import dcclib.mayalib as ml

# To get dcclib maya modules info
ml._modules(ml)             # List custom dcclib.mayalib modules
ml._modules(ml, all=True)   # List all modules in dcclib.mayalib


ml.scene.get_scene_name()
ml.scene.get_workspace_path()
```

#### BLENDER



