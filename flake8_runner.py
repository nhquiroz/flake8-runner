#!/usr/bin/python

# <--- modules needed --->

import sys
import glob
import subprocess
from colorama import Fore, init
init()


# <--- aux functions --->

error_counter = 0   # global counter


def run_flake8_on_file(filename):
    flake8_exit_code = subprocess.call("flake8 " + str(filename), shell=True)
    if flake8_exit_code != 0:   # flake8_exit_code == 0 means OK
        global error_counter
        error_counter += 1
        return flake8_exit_code
    else:
        print(Fore.GREEN + "%r... OK.") % filename


def create_py_list_from_directory():
    # create list of .py files from current directory
    script_list = []

    for file in glob.glob("*.py"):
        if file != 'flake8_runner.py':
            script_list.append(file)

    script_list.sort()
    return script_list


def exit_if_list_is_empty(list):
    if not list:
        print(Fore.RED + "No .py files found. Try another directory.")
        sys.exit()


def print_results():
    if error_counter > 0:
        print(Fore.RED + "\n" + "Finished. Some errors found.")
    else:
        print("\n" + "Finished. All scripts have passed flake8!")


# <--- beginning of the script --->

def flake8_runner():
    py_list = create_py_list_from_directory()
    exit_if_list_is_empty(py_list)
    list_size = str(len(py_list))

    print(list_size + " files to be analyzed: " + "\n")
    # run flake8 for every .py file on the current directory
    for script in py_list:
        run_flake8_on_file(script)

    print_results()

flake8_runner()
