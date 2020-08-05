"""
Functions related to nuke nodes
"""
import nuke
import nukescripts

def isEnabled(node):
    """
    Check if the Node is Enabled / Disable
    :param node:
    :return: 
    """

    if 'disable' in [i.name() for i in node.allKnobs()]:
        return (True if not node['disable'].getValue() else False)
    else:
        print("Disable not available for this node")


def isAnimated(node):
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

def isUsingLifetime(node):
    """
    Check if the Node is using Lifetime or not
    :param node:
    :return:
    """

    if 'useLifetime' in [i.name() for i in node.allKnobs()]:
        return (True if node['useLifetime'].getValue() else False)
    else:
        print("No Lifetime Knob Present in the Node")


# ___________ KNOBS ________________________________
# TODO
def listKnobs(node):
    """
    get the list of all knobs that are present in this node.
    :param node:
    :return:
    """
    pass

def getAnimatedKnobs(node):
    """
    returns the list of knobs that are ANIMATED in a node
    :param node:
    :return:
    """
    return [n.name() for n in node.allKnobs() if node['%s' % n.name()].isAnimated()]

def getExpressionDrivenKnobs(node):
    """
    get the list of knobs that are EXPRESSION DRIVEN in a node
    :param node:
    :return:
    """
    return [n.name for n in node.allKnobs() if node['%s' % n.name()].hasExpression()]

def removeAnimationAllKnobs(node):
    """
     Remove Animation on all knobs.
    :param node:
    :return:
    """
    for n in node.allKnobs():
        node['%s' % n.name()].clearAnimated()

def removeAnimationOnKnob(node, knobName):
    """
    === Knob > RC > No Animation
    :param node:
    :param knobName:
    :return:
    """
    node['%s' % knobName].clearAnimated()

# TODO
def bakeAnimationForKnob(knobName):
    """
    === Select Curve > Edit > Generate
    :param knobName:
    :return:
    """
    pass

# TODO
def bakeExpressionForKnob(knobName):
    """
    === Bake Expression Driven Animation into keys
    :param knobName:
    :return:
    """
    pass

def getAllInputs(node):
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

# TODO
def getAllOutputs(node):
    pass

# TODO
def getLabelKnobValue(node, knob):
    pass

# TODO
def setNodeColor(node, color, rgb=None, hsl=None, tmi=None):
    """
    Set the color of the node
    color presets:
        red
        green
        blue : 0xffff
    This is currently taking hexadecimal value, cause of the node.setValue
    Check if RGB/HSV/TMI values can be used as inputs (since that will be more beneficial for artists)
    :param node:
    :return:
    """
    node['tile_color'].setValue(0xffff)
    pass

# TODO
def setLabelColor(node):
    pass

# TODO
def listAllNodePresets(node):
    pass