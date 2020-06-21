# dcclib

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

#NUKE
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
# MAYA
``` python
from dcclib.mayalib import MayaLib
mayascene = MayaLib().mayascene

mayascene.get_scene_name()
mayascene.get_workspace_path()
```




