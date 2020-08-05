"""

"""


class NukeNode(object):
    def __init__(self):
        pass

    def is_enabled(self, node):
        ''' Check if the Node is Enabled / Disable'''
        if 'disable' in [i.name() for i in node.allKnobs()]:
            return (True if not node['disable'].getValue() else False)
        else:
            print
            "Disable not available for this node"

    def is_animated(self, node):
        ''' Check if the Node is Animated or not'''
        animated_knobs = []
        for knob in node.allKnobs():
            if knob.isAnimated():
                animated_knobs.append(knob.name())
        return (True if animated_knobs else False)

    def is_using_lifetime(self, node):
        ''' Check if the Node is using Lifetime or not'''
        if 'useLifetime' in [i.name() for i in node.allKnobs()]:
            return (True if node['useLifetime'].getValue() else False)
        else:
            print
            "No Lifetime Knob Present in the Node"

    def get_animated_knobs(self, node):
        ''' returns the list of knobs that are ANIMATED in a node'''
        return [n.name() for n in node.allKnobs() if node['%s' % n.name()].isAnimated()]

    def get_expression_driven_knobs(self, node):
        ''' returns the list of knobs that are EXPRESSION DRIVEN in a node'''
        return [n.name for n in node.allKnobs() if node['%s' % n.name()].hasExpression()]

    def no_animation_on_all_knobs(self, node):
        ''' === Node > RC > No Animation on all knobs'''
        for n in node.allKnobs():
            node['%s' % n.name()].clearAnimated()

    def no_animation_on_knob(self, node, knobName):
        ''' === Knob > RC > No Animation'''
        node['%s' % knobName].clearAnimated()

    def bake_animation_of_knob(self, knobName):
        ''' === Select Curve > Edit > Generate'''
        pass

    def bake_expression(self, knobName):
        ''' === Bake Expression Driven Animation into keys'''
        pass

    def get_input_nodes_name(self, node):
        ''' Returns the list of names of input nodes connected to the given node'''
        node_list = []
        for each in range(node.inputs()):
            try:
                node_list.append(node.input(each).name())
            except:
                pass
        return node_list

