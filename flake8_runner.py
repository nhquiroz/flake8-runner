#!/usr/bin/python

"""
A simple script that runs flake8 on every .py file, from the current directory.
Nicolas Quiroz
https://github.com/nhquiroz/flake8-runner
GPL v2.0 License.
"""

# <--- modules needed --->

import glob
import subprocess
from colorama import Fore, init
init()


# <--- colors --->

GREEN = Fore.GREEN
RED = Fore.RED


# <--- aux functions --->

def run_flake8_on(py_file):
    """
    Runs 'flake8' command on 'py_file' passed as argument and returns a
    Boolean value, indicating if any issue is found.
    flake8_exit_code contains the exit code from calling 'flake8' command with
    'py_file' as argument. If flake8_exit_code equals 0, there are no errors
    and an 'OK' legend will be printed. Otherwise, the issue is reported.
    """

    issues = False
    flake8_exit_code = subprocess.call("flake8 " + str(py_file), shell=True)
    if flake8_exit_code != 0:
        issues = True
    else:
        print("{0}{1!r}... OK.".format(GREEN, py_file))

    return issues


def create_py_gen_from_directory():
    """
    Returns a generator, to iterate over all the existent .py files on the
    current directory (except for this script).
    """

    py_gen = (py for py in glob.glob("*.py") if py != 'flake8_runner.py')

    return py_gen


def exit_if_gen_is_empty(py_gen):
    """
    If the iterator passed as argument is empty (None), this functions prints
    an error message and stops the execution of the script.
    """

    try:
        next(py_gen)
    except StopIteration:
        print("{0}No '*.py' files found. Try another directory.".format(RED))
        import sys
        sys.exit()


def show_results(issues):
    """
    Prints the result, after all the files from the current directory
    have been analyzed. If any issue is found, it shows a warning message.
    """

    if issues:
        print("{0}\nWARNING: Some issues found.".format(RED))
    else:
        print("\nOK! All scripts have passed flake8.")


# <--- beginning of the script --->

def main():
    """
    This is the main function of the script. It iterates over all the .py
    files from the current directory and applies the 'flake8' command to each.
    Finally, it prints the results.
    """

    issues_found = False

    py_gen = create_py_gen_from_directory()
    exit_if_gen_is_empty(py_gen)

    for py_file in py_gen:
        issues_found = run_flake8_on(py_file)

    show_results(issues_found)

main()
