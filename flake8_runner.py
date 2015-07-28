#!/usr/bin/python

# <--- modules needed --->

import sys
import glob
import subprocess
from colorama import Fore, init
init()


# <--- color constants --->

GREEN = Fore.GREEN
RED = Fore.RED


# <--- aux functions --->

def run_flake8_on(py_file):
    """
    Runs 'flake8' command on 'py_file' passed as argument.
    flake8_exit_code contains the exit code from calling 'flake8' command with
    'py_file' as argument. If flake8_exit_code is equal to zero, it means there
    are no errors and an 'OK' legend will be printed.
    Otherwise, the issue is reported.
    """

    issues = 0
    flake8_exit_code = subprocess.call("flake8 " + str(py_file), shell=True)
    if flake8_exit_code != 0:
        issues = 1
        return flake8_exit_code
    else:
        print("{}{!r}{}".format(GREEN, py_file, "... OK."))

    return issues


def create_py_list_from_directory():
    """
    Creates a list from .py files present on the current directory (except
    for this script) and returns the list sorted.
    """

    script_list = []

    for py_file in glob.glob("*.py"):
        if py_file != 'flake8_runner.py':
            script_list.append(py_file)

    script_list.sort()
    return script_list


def exit_if_list_is_empty(py_list):
    """
    If the list passed as argument is empty, this functions prints an error
    message and stops the execution of the script.
    """

    if not py_list:
        print("{}{}".format(RED, "No .py files found. Try another directory."))
        sys.exit()


def show_results(issues):
    """
    Prints the result, after all the files from the current directory
    have been analyzed. If issues are found, shows the quantity.
    """

    if issues > 0:
        print("{}{}{}".format(RED, "\n", "Finished. ", issues,
              " issues found."))
    else:
        print("{}{}".format("\n", "Finished. All scripts have passed flake8!"))


# <--- beginning of the script --->

def main():
    """
    This is the main function of the script. It initializes the
    issues_found global variable to zero, then list all the .py
    files from the current directory and finnaly applies the 'flake8'
    command to each.
    """

    issues_found = 0

    py_list = create_py_list_from_directory()
    exit_if_list_is_empty(py_list)
    n = len(py_list)

    print("{} {} {}".format(n, "files to be analyzed:", "\n"))

    for script in py_list:
        issues_found += run_flake8_on(script)

    show_results(issues_found)

main()
