from maya import cmds
import pymel.core as pm



def getShadingMaps():
    """
    Get shadingSG maps from maya file.
    :return: The dict to describe the relationship between geometries with
    shaders, e.g.
    {'lambert3SG': ['|pCube3.f[4]', '|pCube2|pCubeShape2'],
     'lambert2SG': ['|pCube1|pCubeShape1']}
    :rtype: dict
    """
    shadingMaps = {}
    defaultShadingEngines = ['initialParticleSE', 'initialShadingGroup']
    shadingEngines = cmds.ls(type='shadingEngine', l=True)
    for shadingEngine in shadingEngines:
        if shadingEngine in defaultShadingEngines:
            continue
        members = []
        if cmds.sets(shadingEngine, q=1):
            for i in cmds.sets(shadingEngine, q=1):
                members.append(str(i))
            if not members:
                continue
            sets = []
            for member in members:
                if '.f[' in member:
                    meshName = member.split('.')
                    member = cmds.ls(meshName[0], l=1)[0] + '.' + meshName[1]
                else:
                    member = cmds.ls(member, l=1)[0]
                sets.append(member)
            if not sets:
                continue
            else:
                shadingMaps.update({shadingEngine: sets})

    return shadingMaps