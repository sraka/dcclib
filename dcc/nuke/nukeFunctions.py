readGeo = nuke.createNode('ReadGeo2', 'file {alembicFile.abc}')
readGeo.hideControlPanel()
sceneView = readGeo['scene_view']

allItems = sceneView.getAllItems()
sceneView.setImportedItems(allItems)
sceneView.setSelectedItems(allItems)

--------------------------------------------------------------------------------------
# Rename ReadGeo nodes by Alembic SceneGraph\

nuke.createNode('ReadGeo', 'file {/Users/swift/Desktop/scene.abc}') 

def AlembicRename():
    for s in nuke.allNodes('ReadGeo4'):
        sceneView = s['scene_view']
        fullHierarchy = sceneView.getAllItems()
        print fullHierarchy

AlembicRename()
