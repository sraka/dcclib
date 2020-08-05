# dcclib

## Project Goals

## Who is dcclib for?

### For the Novice
### For Technical Director


examples:
Usage in Python Scripts
``` python
from dcclib.mayalib import MayaLib
mayalib = MayaLib()

from dcclib.nukelib import NukeLib
nukelib = NukeLib()
nukelib.nukescene.test()
nukelib.nukescene.delete_all_nodes()
nukelib.nukescene.deselect_all_nodes()
```
Usage inside the DCC appliacation.
Load like this when lauching DCC application

#### NUKE
Place these inside the init.py file of nuke.
``` python
from dcclib.nukelib import NukeLib
nukescene = NukeLib().nukescene
nukevray = NukeLib().nukevray
nukenode = NukeLib().nukenode 
nukegui = NukeLib().nukegui

nukescene.deselect_all_nodes()
nukegui.NukeWindow()
nukevray.list_vray_nodes()
```
#### MAYA
Place this inside the userSetup.py file of maya.
``` python
from dcclib.mayalib import MayaLib
mayascene = MayaLib().mayascene

mayascene.get_scene_name()
mayascene.get_workspace_path()
```

#### BLENDER



