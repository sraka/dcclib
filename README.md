# dcclib

## Project Goals

## Who is dcclib for?

### For the Novice
### For Technical Director


examples:
Usage in Python Scripts
``` python
import dcclib.mayalib as ml
import dcclib.nukelib as nl
import dcclib.blenderlib as bl
```
Usage inside the DCC appliacation.
Load like this when lauching DCC application

#### NUKE
Place these inside the init.py file of nuke.
``` python
import dcclib.nukelib as nl

nl.scene.test()
nl.scene.delete_all_nodes()
nl.scene.deselect_all_nodes()

nl.gui.NukeWindow()

nl.vray.list_vray_nodes()
```

#### MAYA
Place this inside the userSetup.py file of maya.
``` python
import dcclib.mayalib as ml

# To get dcclib maya modules info
ml._modules(ml)
ml._modules(ml, all=True)


mayascene.get_scene_name()
mayascene.get_workspace_path()
```

#### BLENDER



