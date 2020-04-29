import getpass
import os
import shutil
import sys
import webbrowser


def get_username():
    username = os.environ.get('USER')

    if sys.platform == "win32":
        username = os.environ.get('USERNAME')

    return username


def get_user_home():
    user_home = os.environ.get('HOME')

    if sys.platform == "win32":
        user_home = os.environ.get('USERPROFILE')

    return user_home


def get_user_credentials():
    user_name = raw_input('Enter user name:').rstrip()
    password = getpass.getpass()

    return user_name, password


def get_env_sep():
    if sys.platform == "win32":
        return ";"
    else:
        return ":"


def get_platform():
    if sys.platform == "win32":
        return "windows"
    elif sys.platform == "darwin":
        return "mac"
    elif sys.platform == "linux" or sys.platform == "linux2":
        return "linux"


def open_url(path):
    if sys.platform == "darwin":
        path = "file:///" + path
    webbrowser.open(path)


def open_path_in_file_browser(path):
    if os.path.isdir(path):
        if get_platform() == 'windows':
            os.startfile(path)
        elif get_platform() == 'mac':
            print("Function not defnied for linux")
        elif get_platform() == 'linux':
            try:
                os.system('xdg-open {}'.format(path))
            except:
                raise ValueError('Function not working as expected')
    else:
        raise ValueError('Path is not a directory')


def remove_directory_contents(directory):
    for path in os.listdir(directory):
        file_path = os.path.join(directory, path)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def ensure_directories(list_of_directories):
    """
    Create the directories if they don't exist

    :param list_of_directories: List of directory names to be checked
    :type list_of_directories: list
    """
    for dir_name in list_of_directories:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
