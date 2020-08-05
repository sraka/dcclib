
class BlenderInfo(object):

    def __init__(self):
        pass

    @staticmethod
    def test():
        print("Blender Info")

    @staticmethod
    def get_blender_version():
        """
        Gives the current blender version.
        :return: A `str` formatted like: "2.79.0"
        """
        return ".".join([str(i) for i in bpy.app.version])