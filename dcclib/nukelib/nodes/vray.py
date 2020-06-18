"""

"""



class NukeVray(object):
    def __init__(slef):
        print(__name__)

    def test(self):
        print("Nuke Vray")

    def list_vray_nodes(self):
        return [node.name() for node in nuke.allNodes() if 'VRay' in node.Class()]