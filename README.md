# flake8-runner

[![Code Climate](https://codeclimate.com/github/nhquiroz/flake8-runner/badges/gpa.svg)](https://codeclimate.com/github/nhquiroz/flake8-runner)

![screenshot](https://github.com/nhquiroz/flake8-runner/blob/master/screenshots/test-ok.png)

## Overview

A simple python (2.7.6) script that runs flake8 on every .py file, from the current directory.  

Flake8 is a static analysis and syntax checking tool. It works as a wrapper around these tools:

- [PyFlakes](https://pypi.python.org/pypi/pyflakes)
- [pep8](https://pypi.python.org/pypi/pep8)
- [Ned Batchelder’s McCabe script](https://pypi.python.org/pypi/mccabe)

Flake8 runs all the tools by launching the single flake8 script. It displays the warnings in a per-file, merged output.  

## Installation
In order to be able to use it, you need to:  

1. [Install Python 2.7.x or newer](https://www.python.org/downloads/) (not tested on previous versions).  
2. [Install pip](https://pip.pypa.io/en/latest/installing.html).    
3. [Install the flake8 package](https://pypi.python.org/pypi/flake8).  

## Usage

```
$ pip install flake8
$ cd /py-files-directory
$ python flake8-runner.py
```
