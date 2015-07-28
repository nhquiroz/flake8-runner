# flake8-runner

[![Code Climate](https://codeclimate.com/github/nhquiroz/flake8-runner/badges/gpa.svg)](https://codeclimate.com/github/nhquiroz/flake8-runner)

## Overview

A simple python (2.7.6) script that runs flake8 on every .py file, from the current directory.  

Flake8 is a wrapper around these tools:

    PyFlakes
    pep8
    Ned Batchelder’s McCabe script

Flake8 runs all the tools by launching the single flake8 script. It displays the warnings in a per-file, merged output.  

## Installation
In order to be able to use it, you need to [install](https://pip.pypa.io/en/latest/installing.html) `pip` first.  
Then, install the [flake8 package](https://pypi.python.org/pypi/flake8).

## Usage

```
$ pip install flake8
$ cd /py-files-directory
$ python flake8-runner.py
```

## Screenshots

