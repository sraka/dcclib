import os
import yaml

def read_yaml(filepath, safe_load=True):
    """
    :param filepath:
    :return
    """
    if os.path.isdir(filepath) or "." not in os.path.basename(filepath):
        raise ValueError("Path given must be a filepath , not a directory")

    if not os.path.exists(filepath):
        raise ValueError("Given filepath {} does not exists.".format(filepath))

    if safe_load:
        with open(filepath, "r") as reader:
            yaml_data = yaml.safe_load(reader)
    if not safe_load:
        with open(filepath, "r") as reader:
            yaml_data = yaml.load(reader)

    return yaml_data

def write_yaml(data, filepath, force=False):
    """
        :param data:
        :param filepath:
        :param indent:
        :param force:
        :return:
        """
    if type(data) != dict and type(data) != list:
        raise ValueError("Info cannot be {}. It must be a dictionary type".format(type(data)))

    if os.path.isdir(filepath) or "." not in os.path.basename(filepath):
        raise ValueError("filepath {} must be a path of the file , not a directory".format(type(data)))

    if os.path.exists(filepath) and not force:
        raise ValueError("filepath already exists , use --force to overwrite")

    elif os.path.exists(filepath) and force:
        try:
            os.remove(filepath)
        except Exception as error:
            raise ValueError("Failed to remove existing file {} \n {} ".format(filepath, str(error)))

    if not os.path.exists(filepath):
        try:
            os.mkdir(os.path.dirname(filepath))
        except Exception as error:
            raise ValueError("Failed to create folders for following path {} ".format(str(error)))

    with open(filepath, "w") as writer:
        yaml.dump(data, writer, default_flow_style=False, explicit_start=True)

    return filepath


