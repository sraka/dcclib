import os
import sys
import pymel.core as pm
import maya.cmds as cmds


def get_render_layers(mode=None):
    '''
        Args: 
            mode = the mode of data is req to be returned , default it will return the obj mode
        ex:
            mayaRendering.get_render_layers('list')     # Will Return the list of data
    '''
    if mode == 'list':
        return [each.name() for each in pm.ls(mode="renderLayer") if each.name() != 'defaultRenderLayer']
    else:
        return [each for each in pm.ls(mode="renderLayer") if each.name() != 'defaultRenderLayer']

def set_renderable_all(state):
    """ 
        Info:
            Sets renderable status for all the render layers in the file
        Args:
            state = True/False , if True (Enable) , if Flase (Disable)
        ex:
            mayaRendering.set_renderable_all(0)
            mayaRendering.set_renderable_all(False)
    """
    rlys = get_render_layers()
    if state:
        for each in rlys:
            each.attr('renderable').set(1)
    else:
        for each in rlys:
            each.attr('renderable').set(0)

def set_renderable_current(state):
    """
        Info:
            Sets renderable status for currewnt render layer
        Args:
            state = True/False , if True (Enable) , if Flase (Disable)     
    """
    cur_rly = pm.editRenderLayerGlobals(q=1,crl=1)
    if state:
        pm.setAttr('{}.renderable'.format(cur_rly),1)
    else:
        pm.setAttr('{}.renderable'.format(cur_rly),0)

def get_renderer():
    return pm.getAttr("defaultRenderGlobals.currentRenderer")

def set_renderer(render_engine_name):
    """ 
        Args:   render_engine_name = 'arnold' / 'redshift' / 'vray' / 'mayaSoftware' / 'mayaHardware' / 'mayaHardware2' / 'mayaVector' / mentalray

        eg:     mayaRendering.set_renderer('vray')
    """
    if render_engine_name == 'arnold':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))
    elif render_engine_name == 'redshift':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))
    elif render_engine_name == 'vray':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))
    elif render_engine_name == 'mayaSoftware':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))
    elif render_engine_name == 'mayaHardware':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))
    elif render_engine_name == 'mayaHardware2':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))
    elif render_engine_name == 'mayaVector':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))
    elif render_engine_name == 'mentalray':
        pm.setAttr("defaultRenderGlobals.currentRenderer",str(render_engine_name))

def get_render_path():
    return pm.renderSettings(fp=1,fin=1)[0]

def get_render_directory():
    return os.path.dirname(get_render_path())