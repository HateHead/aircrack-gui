import os
import shutil


def isDir(path: str) -> bool:
    return os.path.isdir(path)


def isFile(path: str) -> bool:
    return os.path.isfile(path)


def rmDirContents(path: str) -> None:
    if not isDir(path):
        raise Exception(f"Folder does not exist: {path}")

    for root, dirs, files in os.walk(path):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))


def rmDir(directory: str) -> None:

    if not isDir(directory):
        raise Exception(f"{directory} does not exist!")

    shutil.rmtree(directory)


def createDir(directory: str) -> None:
    os.makedirs(directory)


def listFoldersInDir(directory: str) -> list[str]:
    """Lists folders in directory"""

    if not isDir(directory):
        raise Exception(f"{directory} does not exist!")

    return [dir for dir in os.listdir(directory) if isDir(os.path.join(directory, dir))]


def listFilesInDir(directory: str) -> list[str]:
    """Lists files in directory"""

    return [
        file for file in os.listdir(directory) if isFile(os.path.join(directory, file))
    ]
