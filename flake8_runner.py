#!/usr/bin/python

# <--- modules needed --->

import glob
import subprocess
from colorama import Fore, init
init()


# <--- aux functions --->

def run_flake8_on_file(filename):
    flake8_exit_code = subprocess.call("flake8 " + str(filename), shell=True)
    if flake8_exit_code != 0:   # flake8_exit_code == 0 means OK
        return flake8_exit_code
    print(Fore.GREEN + "%r flake8... OK.\n") % filename


def create_py_list_from_directory():
    # create list of .py files from current directory
    script_list = []

    for file in glob.glob("*.py"):
        if file != 'flake8_runner.py':
            script_list.append(file)

    script_list.sort()
    return script_list


# <--- beginning of the script --->

def flake8_runner():
    py_list = create_py_list_from_directory()
    if not py_list:
        print(Fore.RED + "No .py files found.")
        raise SystemExit    # stops execution and raise SystemExit exception

    print(str(len(py_list)) + " .py scripts to be executed: " + ".\n")

    # run flake8 for every .py file on the current directory
    for script in py_list:
        run_flake8_on_file(script)

    print("> All scripts have passed flake8!")

flake8_runner()
