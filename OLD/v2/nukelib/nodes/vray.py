"""

"""



class NukeVray(object):
    def __init__(slef):
        print(__name__)

    @staticmethod
    def test():
        print("Nuke Vray")

    @staticmethod
    def list_vray_nodes():
        return [node.name() for node in nuke.allNodes() if 'VRay' in node.Class()]