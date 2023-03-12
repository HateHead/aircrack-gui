import os


def run_command(command):
    """Runs sync command"""
    return os.popen(command).read()


def run_command_background(command):
    """Runs command async"""
    return os.popen(command)
