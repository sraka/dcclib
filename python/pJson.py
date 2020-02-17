import os
import json

def write_json(info,filepath,indent=2,force=False):
    """

    :param info:
    :param filepath:
    :param indent:
    :param force:
    :return:
    """
    if type(info) != dict and type(info) != list:
        raise ValueError ("Info cannot be {}. It must be a dictionary type".format(type(info)))

    if os.path.isdir(filepath) or "." not in os.path.basename(filepath):
        raise ValueError ("filepath {} must be a path of the file , not a directory".format(type(info)))

    if os.path.exists(filepath) and not force:
        raise ValueError("filepath already exists , use --force to overwrite")

    elif os.path.exists(filepath) and force:
        try:
            os.remove(filepath)
        except Exception as error:
            raise ValueError ("Failed to remove existing file {} \n {} ".format(filepath , str(error)))

    if not os.path.exists(filepath):
        try:
            os.mkdir(os.path.dirname(filepath))
        except Exception as error:
            raise ValueError("Failed to create folders for following path {} ".format(str(error)))

    with open(filepath ,"w") as writer:
        json.dump(info, writer, sortkeys=True, indent = indent)

    return filepath

def read_json(filepath):
    """

    :param filepath:
    :return:
    """
    if os.path.isdir(filepath) or "." not in os.path.basename(filepath):
        raise ValueError ("Path given must be a filepath , not a directory")

    if not os.path.exists(filepath):
        raise ValueError ("Given filepath {} does not exists.".format(filepath))

    with open(filepath , "r") as reader:
        json_data = json.load(reader)
    return json_data

