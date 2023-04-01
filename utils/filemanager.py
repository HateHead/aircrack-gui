import os
import shutil


def is_dir(path: str) -> bool:
    """Retursn True if the directory exists"""
    return os.path.isdir(path)


def is_file(path: str) -> bool:
    """Returns True if the file exists"""
    return os.path.isfile(path)


def rm_dir_contents(directory: str) -> None:
    """Clears directory"""
    if not is_dir(directory):
        raise NotADirectoryError(f"Directory does not exist: {directory}")

    for root, dirs, files in os.walk(directory):
        for _file in files:
            os.unlink(os.path.join(root, _file))
        for _dir in dirs:
            shutil.rmtree(os.path.join(root, _dir))


def rm_dir(directory: str) -> None:
    """Deletes direcotry and its contents"""
    if not is_dir(directory):
        raise NotADirectoryError(f"Directory does not exist: {directory}")

    shutil.rmtree(directory)


def create_dir(directory: str) -> None:
    """Creates ampty directory"""
    os.makedirs(directory)


def list_folders_in_dir(directory: str) -> list[str]:
    """Lists folders in directory"""

    if not is_dir(directory):
        raise NotADirectoryError(f"Directory does not exist: {directory}")

    return [
        dir for dir in os.listdir(directory) if is_dir(os.path.join(directory, dir))
    ]


def list_files_in_dir(directory: str) -> list[str]:
    """Lists files in directory"""

    if not is_dir(directory):
        raise NotADirectoryError(f"Directory does not exist: {directory}")

    return [
        file for file in os.listdir(directory) if is_file(os.path.join(directory, file))
    ]
