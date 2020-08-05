"""

"""

def list_selected_nodes(name=False):
    """
    Returns the list os selected nodes
    :return:
    """
    if name:
        return [node.name() for node in nuke.allNodes() if node.isSelected()]
    else:
        return [node for node in nuke.allNodes() if node.isSelected()]

def list_disabled_nodes():
    """
    Returns the list of disabled nodes present in the flow
    :return:
    """
    disabled_nodes = []
    for node in nuke.allNodes():
        if 'disable' in [i.name() for i in node.allKnobs()]:
            if node['disable'].getValue():
                disabled_nodes.append(node.name())
    return disabled_nodes

def list_floating_nodes():
    """
    Returns the list of nodes that are floating
    :return:
    """
    skipNodeTypes = ['Viewer', 'BackdropNode']
    return [node.name() for node in nuke.allNodes() if
            not node.dependent() and not node.dependencies() and not node.Class() in skipNodeTypes]

def list_group_nodes():
    """
    Returns the list of Group Nodes in the flow
    :return:
    """
    return [node.name() for node in nuke.allNodes('Group')]

def list_animated_nodes():
    """
    Returns the list of all Animated Nodes in the flow
    :return:
    """
    animated_nodes = []
    for node in nuke.allNodes():
        for knob in node.allKnobs():
            if knob.isAnimated():
                animated_nodes.append(node.name())
    return animated_nodes

def list_expression_driven_nodes():
    """
    Returns the list of all Expression Driven Nodes in the flow
    :return:
    """
    exp_driven_nodes = []
    for node in nuke.allNodes():
        for knob in node.allKnobs():
            if knob.hasExpression():
                exp_driven_nodes.append(node.name())
    return exp_driven_nodes

# --------------------------------------------------- DELETE FUNCTIONS ---------------------------------------------
# ------------------------------------------------------------------------------------------------------------------
def delete_floating_nodes():
    """

    :return:
    """
    skipNodeTypes = ['Viewer', 'BackdropNode']
    [nuke.delete(node) for node in nuke.allNodes() if not node.dependent() and not node.dependencies() and not node.Class() in skipNodeTypes]

def delete_viewer_nodes():
    """

    :return:
    """
    [nuke.delete(node) for node in nuke.allNodes() if node.Class() == 'Viewer']

def delete_empty_backdrop_nodes(self):
    pass
    # for node in nuke.allNodes():
    # if node.Class == 'BackdropNode':
    # node.selectNodes()

# --------------------------------------------------- MISC FUNCTIONS -----------------------------------------------
# ------------------------------------------------------------------------------------------------------------------

def list_nodes():
    """

    :return:
    """
    return [node.name() for node in nuke.allNodes()]

def deselect_all_nodes():
    """

    :return:
    """
    for node in nuke.allNodes():
        node.setSelected(0)
        all = nuke.allNodes()
    # OR
    # for each in nuke.allNodes():
    #     node = nuke.toNode(each.name())
    #     node['selected'].setValue(False)

def select_all_nodes():
    """

    :return:
    """
    for node in nuke.allNodes():
        node.setSelected(1)
    # OR
    # for each in nuke.allNodes():
    #     node = nuke.toNode(each.name())
    #     node['selected'].setValue(1)

def delete_all_nodes():
    """

    :return:
    """
    [nuke.delete(each) for each in nuke.allNodes()]

def reopen_scene():
    """

    :return:
    """
    scene_name = nuke.root().name()
    nuke.scriptClose(scene_name)
    nuke.scriptOpen(scene_name)

def get_scene_name():
    """

    :return:
    """
    return nuke.root().name().split('.')[0].split('/')[-1]

def get_scene_path():
    """

    :return:
    """
    return nuke.scriptName()
