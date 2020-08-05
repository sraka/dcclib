"""

"""


def is_enabled(node):
    """
    Check if the Node is Enabled / Disable
    :param node:
    :return: 
    """

    if 'disable' in [i.name() for i in node.allKnobs()]:
        return (True if not node['disable'].getValue() else False)
    else:
        print
        "Disable not available for this node"

def is_animated(node):
    """
    Check if the Node is Animated or not
    :param node:
    :return:
    """

    animated_knobs = []
    for knob in node.allKnobs():
        if knob.isAnimated():
            animated_knobs.append(knob.name())
    return (True if animated_knobs else False)

def is_using_lifetime(node):
    """
    Check if the Node is using Lifetime or not
    :param node:
    :return:
    """

    if 'useLifetime' in [i.name() for i in node.allKnobs()]:
        return (True if node['useLifetime'].getValue() else False)
    else:
        print
        "No Lifetime Knob Present in the Node"

# ___________ KNOBS ________________________________
def list_knobs(node):
    """
    get the list of all knobs that are present in this node.
    :param node:
    :return:
    """
    pass

def get_animated_knobs(node):
    """
    returns the list of knobs that are ANIMATED in a node
    :param node:
    :return:
    """
    return [n.name() for n in node.allKnobs() if node['%s' % n.name()].isAnimated()]

def get_expression_driven_knobs(node):
    """
    get the list of knobs that are EXPRESSION DRIVEN in a node
    :param node:
    :return:
    """
    return [n.name for n in node.allKnobs() if node['%s' % n.name()].hasExpression()]

def no_animation_on_all_knobs(node):
    """
     Remove Animation on all knobs.
    :param node:
    :return:
    """
    for n in node.allKnobs():
        node['%s' % n.name()].clearAnimated()

def no_animation_on_knob(node, knobName):
    """
    === Knob > RC > No Animation
    :param node:
    :param knobName:
    :return:
    """
    node['%s' % knobName].clearAnimated()

def bake_animation_of_knob(knobName):
    """
    === Select Curve > Edit > Generate
    :param knobName:
    :return:
    """
    pass

def bake_expression_of_knob(knobName):
    """
    === Bake Expression Driven Animation into keys
    :param knobName:
    :return:
    """
    pass

def get_all_inputs(node):
    """
    Returns the list of names of input nodes connected to the given node
    :param node:
    :return:
    """
    node_list = []
    for each in range(node.inputs()):
        try:
            node_list.append(node.input(each).name())
        except:
            pass
    return node_list

def get_all_outputs(node):
    pass

def get_label_knob_value(node, knob):
    pass