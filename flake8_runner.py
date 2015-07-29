#!/usr/bin/python

"""
A simple script that runs flake8 on every .py file, from the current directory.
Nicolas Quiroz
https://github.com/nhquiroz/flake8-runner
GPL v2.0 License.
"""


import glob
import subprocess
from colorama import Fore, init
init()


def run_flake8_on(py_file):
    """
    Runs 'flake8' command on 'py_file' passed as argument and returns a
    Boolean, indicating if any issue is found. flake8_exit_code variable
    contains the exit code from calling 'flake8' command with 'py_file'
    as argument. If flake8_exit_code equals 0, there are no errors and
    an 'OK' legend will be printed. Otherwise, the issue is reported.
    """

    issues = False
    flake8_exit_code = subprocess.call("flake8 " + str(py_file), shell=True)
    if flake8_exit_code != 0:
        issues = True
    else:
        print("{!r}... OK.".format(py_file))

    return issues


def py_gen_from():
    """
    Returns a generator to iterate over all the existent .py files on
    the current directory (except for this script).
    """

    return (py for py in glob.glob("*.py") if py != 'flake8_runner.py')


def exit_if_empty(py_gen):
    """
    Stops the execution and shows a message if the iterator passed as
    argument is empty (references to None).
    Otherwise, the iterator is reseted.
    """

    try:
        py_gen.next()
    except StopIteration:
        print("{}No '*.py' files found in this directory.".format(Fore.RED))
        import sys
        sys.exit()
    else:
        py_gen = py_gen_from()
        return py_gen


def show_results(issues):
    """
    Prints the result, after all the files from the current directory
    have been analyzed. If any issue is found, it shows a warning message.
    """

    if issues:
        print("{0}\nWARNING: Some issues found.".format(Fore.RED))
    else:
        print("{0}\nOK! All scripts have passed flake8.".format(Fore.GREEN))


#   beginning of the script

def main():
    """
    This is the main function of the script. It iterates over all the .py
    files from the current directory and applies the 'flake8' command to each.
    Finally, it prints the results.
    """

    first_gen = py_gen_from()
    second_gen = exit_if_empty(first_gen)

    issues_found = False
    for py_file in second_gen:
        issues_found = issues_found or run_flake8_on(py_file)

    show_results(issues_found)

main()
