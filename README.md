# flake8-runner
A simple python (2.7.6) script that runs flake8 on every .py file, from the current directory.  

Flake8 is a wrapper around these tools:

    PyFlakes
    pep8
    Ned Batchelder’s McCabe script

Flake8 runs all the tools by launching the single flake8 script. It displays the warnings in a per-file, merged output.  


In order to be able to use it, you need to [install](https://pip.pypa.io/en/latest/installing.html) `pip` first.  

Then, just install [flake8](https://pypi.python.org/pypi/flake8) and run the script:  
```
$ pip install flake8
$ cd /py-files-directory
$ python flake8-runner.py
```

