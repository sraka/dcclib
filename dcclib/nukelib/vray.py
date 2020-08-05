"""

"""


def test():
    print("Nuke Vray")


def list_vray_nodes():
    """

    :return:
    """
    return [node.name() for node in nuke.allNodes() if 'VRay' in node.Class()]
