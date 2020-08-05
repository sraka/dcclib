



class NukeSession(object):
    def __init__(self):
        print(__name__)

    @staticmethod
    def test():
        print("Nuke Session Class initiated")
    # -------------------------------------------------------------- LIST FUNCTIONS -----------------------------------------------------------------------
    # -----------------------------------------------------------------------------------------------------------------------------------------------------
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
        skipNodeTypes = ['Viewer', 'BackdropNode']
        return [node.name() for node in nuke.allNodes() if
                not node.dependent() and not node.dependencies() and not node.Class() in skipNodeTypes]

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