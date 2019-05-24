import os
import sys
import nuke
import nukescripts


'''
import sys
sys.path.append(r'D:/__CS/___HOME_DIR/pipeline/CoreLibrary/moduleNuke')
import nukeClasses as nukeClasses;reload(nukeClasses)
nukescene = nukeClasses.NukeSession()
nukenode = nukeClasses.NukeNode()
nukevray = nukeClasses.NukeVray()
'''
print __name__


class NukeNode(object):
    def __init__(self):
        pass
    
    def is_enabled(self,node):
        ''' Check if the Node is Enabled / Disable'''
        if 'disable' in [i.name() for i in node.allKnobs()]:
            return (True if not node['disable'].getValue() else False)
        else:
            print "Disable not available for this node"
    
    def is_animated(self,node):
        ''' Check if the Node is Animated or not'''
        animated_knobs = []
        for knob in node.allKnobs():
            if knob.isAnimated():
                animated_knobs.append(knob.name())
        return (True if animated_knobs else False)
    
    def is_using_lifetime(self,node):
        ''' Check if the Node is using Lifetime or not'''
        if 'useLifetime' in [i.name() for i in node.allKnobs()]:
            return (True if node['useLifetime'].getValue() else False)
        else:
            print "No Lifetime Knob Present in the Node"
       
    def get_animated_knobs(self,node):
        ''' returns the list of knobs that are ANIMATED in a node'''
        return [n.name() for n in node.allKnobs() if node['%s'%n.name()].isAnimated()]
    
    def get_expression_driven_knobs(self,node):
        ''' returns the list of knobs that are EXPRESSION DRIVEN in a node'''
        return [n.name for n in node.allKnobs() if node['%s'%n.name()].hasExpression()]
    
    def no_animation_on_all_knobs(self,node):
        ''' === Node > RC > No Animation on all knobs'''
        for n in node.allKnobs():
            node['%s'%n.name()].clearAnimated()
            
    def no_animation_on_knob(self , node , knobName):
        ''' === Knob > RC > No Animation'''
        node['%s'%knobName].clearAnimated()
        
    def bake_animation_of_knob(self , knobName):
        ''' === Select Curve > Edit > Generate'''
        pass
    
    def bake_expression(self, knobName):
        ''' === Bake Expression Driven Animation into keys''' 
        pass

    def get_input_nodes_name(self , node):
        ''' Returns the list of names of input nodes connected to the given node'''
        node_list=[]
        for each in range(node.inputs()):
            try:    
                node_list.append(node.input(each).name())
            except:
                pass
        return node_list     
      
class NukeSession(object):
    def __init__(self):
        pass
    #-------------------------------------------------------------- LIST FUNCTIONS -----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    def list_selected_nodes(self):
        ''' Returns the list os selected nodes''' 
        return [node.name() for node in nuke.allNodes() if node.isSelected()]

    def list_disabled_nodes(self):
        ''' Returns the list of disabled nodes present in the flow''' 
        disabled_nodes = []
        for node in nuke.allNodes():
            if 'disable' in [i.name() for i in node.allKnobs()]:
                if node['disable'].getValue():
                    disabled_nodes.append(node.name())
        return disabled_nodes

    def list_floating_nodes(self):
        ''' Returns the list of nodes that are floating''' 
        skipNodeTypes = ['Viewer','BackdropNode']
        return [node.name() for node in nuke.allNodes() if not node.dependent() and not node.dependencies() and not node.Class() in skipNodeTypes]
        
    def list_group_nodes(self):
        ''' Returns the list of Group Nodes in the flow''' 
        return [node.name() for node in nuke.allNodes('Group')]
    
    def list_animated_nodes(self):
        ''' Returns the list of all Animated Nodes in the flow''' 
        animated_nodes = []
        for node in nuke.allNodes():
            for knob in node.allKnobs():
                if knob.isAnimated():
                    animated_nodes.append(node.name())
        return animated_nodes
    
    def list_expression_driven_nodes(self):
        ''' Returns the list of all Expression Driven Nodes in the flow''' 
        exp_driven_nodes = []
        for node in nuke.allNodes():
            for knob in node.allKnobs():
                if knob.hasExpression():
                    exp_driven_nodes.append(node.name())
        return exp_driven_nodes
    
    #-------------------------------------------------------------- DELETE FUNCTIONS -----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    def delete_floating_nodes(self):
        skipNodeTypes = ['Viewer','BackdropNode']
        [nuke.delete(node) for node in nuke.allNodes() if not node.dependent() and not node.dependencies() and not node.Class() in skipNodeTypes]
    
    def delete_viewer_nodes(self):
        [nuke.delete(node) for node in nuke.allNodes() if node.Class() == 'Viewer']
    
    def delete_empty_backdrop_nodes(self):
        pass
        # for node in nuke.allNodes():
            # if node.Class == 'BackdropNode':
                # node.selectNodes()
                
    #-------------------------------------------------------------- MISC FUNCTIONS -----------------------------------------------------------------------
    #-----------------------------------------------------------------------------------------------------------------------------------------------------
    
    def list_nodes(self):
        return [node.name() for node in nuke.allNodes()]
    
    def deselect_all_nodes(self):
        for node in nuke.allNodes():
            node.setSelected(0)
            all = nuke.allNodes()
        # OR            
        # for each in nuke.allNodes():
        #     node = nuke.toNode(each.name())
        #     node['selected'].setValue(False)
    
    def select_all_nodes(self):
        for node in nuke.allNodes():
            node.setSelected(1)
        # OR            
        # for each in nuke.allNodes():
        #     node = nuke.toNode(each.name())
        #     node['selected'].setValue(1)

    def delete_all_nodes(self):
        [nuke.delete(each) for each in nuke.allNodes()]

    def reopen_scene(self):
        scene_name = nuke.root().name()
        nuke.scriptClose(scene_name)
        nuke.scriptOpen(scene_name)

    def get_scene_name(self):
        return nuke.root().name().split('.')[0].split('/')[-1]

    def get_scene_path(self):
        return nuke.scriptName()

class NukeVray(object):
    def __init__(slef):
        pass
        
    def list_vray_nodes(self):
        return [node.name() for node in nuke.allNodes() if 'VRay' in node.Class()]



class MISC():
    def swapOutNode(newNode, targetNode):
    oldSel = []
    if nuke.selectedNodes():
        oldSel = [node for node in nuke.selectedNodes()]
    nukescripts.clear_selection_recursive()
    sourcePos = (newNode.xpos(), newNode.ypos())
    targetPos = (targetNode.xpos(), targetNode.ypos())
    inputNodes = []
    outputNodes = []
    for i in range(targetNode.inputs()):
        inputNodes.append((i, targetNode.input(i)))
    for depNode in nuke.dependentNodes(nuke.INPUTS | nuke.HIDDEN_INPUTS, targetNode):
        for i in range(depNode.inputs()):
            if depNode.input(i) == targetNode:
                outputNodes.append((i, depNode))
                depNode.setInput(i, None)
    targetNode.setSelected(True)
    nuke.extractSelected()
    targetNode.setSelected(False)
    newNode['xpos'].setValue(targetPos[0])
    newNode['ypos'].setValue(targetPos[1])
    targetNode['xpos'].setValue(sourcePos[0])
    targetNode['ypos'].setValue(sourcePos[1])
    for inNode in inputNodes:
        newNode.setInput(inNode[0], inNode[1])
    for outNode in outputNodes:
        outNode[1].setInput(outNode[0], newNode)
    for node in oldSel:
        node.setSelected(True)
    
    
    def lock_knobs(node, node_lock_message='Node_Locked'):
    selNode = node
    allknobs = selNode.allKnobs()
    for knob in allknobs:
        if knob.name() != "Render":
          knob.setEnabled(False)
    labelVal = selNode['label'].getValue()
    labCheck = labelVal.rsplit(None, 1)
    if labCheck:
      labCheck = labCheck[-1]
      if labCheck != node_lock_message:
          selNode['label'].setValue(labelVal+'\n{}'.format(node_lock_message))

    def unlock_knobs(node):
        selNode = node
        allknobs=selNode.allKnobs()
        for knob in allknobs:
            knob.setEnabled(True)
        labelVal = selNode['label'].getValue()
        labCheck = labelVal.rsplit(None, 1)[-1]
        if labCheck == 'Node_Locked':
            newLabel = " ".join(labelVal.split()[:-1])
            selNode['label'].setValue(newLabel)