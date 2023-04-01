from typing import Iterable
import os
import sys
import itertools
import time
import threading

from termcolor import colored

os.system("")


class Spinner:
    """Spinner"""

    spinner: Iterable = []
    delay: float = 0
    busy: bool = False
    spinner_visible: bool = False

    thread: threading.Thread
    _lock: threading.Lock

    def __init__(self, message: str, delay: float = 0.1):
        self.spinner = itertools.cycle(["-", "/", "|", "\\"])
        self.delay = delay
        self.busy = False
        self.spinner_visible = False
        sys.stdout.write(message)

    def write_next(self):
        """Writes next fase"""
        with self._lock:
            if not self.spinner_visible:
                sys.stdout.write(next(self.spinner))  # type: ignore
                self.spinner_visible = True
                sys.stdout.flush()

    def remove_spinner(self, cleanup=False):
        """Clears the line"""
        with self._lock:
            if self.spinner_visible:
                sys.stdout.write("\b")
                self.spinner_visible = False
                if cleanup:
                    sys.stdout.write(" ")  # overwrite spinner with blank
                    sys.stdout.write("\r")  # move to next line
                sys.stdout.flush()

    def spinner_task(self):
        """Creates a spinner task"""
        while self.busy:
            self.write_next()
            time.sleep(self.delay)
            self.remove_spinner()

    def __enter__(self):
        if sys.stdout.isatty():
            self._lock = threading.Lock()
            self.busy = True
            self.thread = threading.Thread(target=self.spinner_task)
            self.thread.start()

    def __exit__(self, exception, value, tb):
        if sys.stdout.isatty():
            self.busy = False
            self.remove_spinner(cleanup=True)
        else:
            sys.stdout.write("\r")


def progress_bar(length: int, percentage: float) -> str:
    """Creates a progress bar where max amount of filled bars = length."""

    if length < 1:
        raise ValueError("Length of progress bar must be greater than 0!")

    if percentage < 0 or percentage > 100:
        raise ValueError("Fill percentage must be in range [0, 100]")

    filled_bars = int(length * percentage / 100)
    return f"[{'=' * filled_bars}{' ' * (length - filled_bars)}]"


def yes_or_no_query(
    question: str, default: bool = True, yes_tooltip: str = "", no_tooltip: str = ""
) -> bool:
    """Creates a yes/no prompt with question, tooltips and default value.
    Returns True/False for yes/no"""

    valid_yes = ["yes", "y"]
    valid_no = ["no", "n"]

    yes_tooltip_text = f": {yes_tooltip} " if yes_tooltip != "" else " "
    no_tooltip_text = f": {no_tooltip}" if no_tooltip != "" else ""

    if default is None:
        prompt = f"\n[y{yes_tooltip_text}/ n{no_tooltip_text}]"
    elif default:
        prompt = f"\n[Y{yes_tooltip_text}/ n{no_tooltip_text}]"
    elif not default:
        prompt = f"\n[y{yes_tooltip_text}/ N{no_tooltip_text}]"
    else:
        raise ValueError(f"Invalid default answer: '{default}'")

    while True:
        log_warning(question + prompt)
        choice = input().lower()
        if default is not None and choice == "":
            return default

        if choice in valid_yes:
            return True

        if choice in valid_no:
            return False

        log_error(
            f"Please respond with {'/'.join(valid_yes)} for yes, {'/'.join(valid_no)} for no.\n"
        )


def up() -> str:
    """Moves caret one line upwards"""
    return "\x1B[1F"


def clear() -> str:
    """Clears line"""
    return "\x1B[0K"


def start_indent() -> str:
    """Retuns start indent"""
    return " - "


def indent(level: int) -> str:
    """Retuns indent multiplied by level"""
    return "   " * level


def log_success(message: str) -> None:
    """Prints green-colored success message"""
    print(colored(message, "green"))


def log_message(message: str, end: str = "\n") -> None:
    """Prints message"""
    print(message, end=end)


def log_warning(warning: str, end: str = "\n") -> None:
    """Prints yellow-colored warning message"""
    print(colored(warning, "yellow"), end=end)


def log_error(error: str, end: str = "\n") -> None:
    """Prints red-colored error message"""
    print(colored(error, "red"), end=end)
