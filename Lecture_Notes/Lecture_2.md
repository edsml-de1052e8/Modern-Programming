## Lecture 2: Python Dev - Scripts, Modules and Packages
***12th October 2021***

There are over 329,000 packages in Python as of early 2021.


Some issues with Python:
Not too good with version control
Sometimes skips cells and doesn’t match cell content
Anaconda: on Windows you can type ```python``` from the Anaconda command prompt to start a basic, no frills python interpreter session. On linux/Mac you may sometimes need to use the command python3 instead.
Python 2 is no longer supported, sometimes happens with older/bigger computers/interpreters

#### IPython
Stands for interactive Python 
To ameliorate python interpreter
Better history editor, quicker help, better tab completions

Rot-13 cypher: don’t use it for coding, just text (tho purposefully hard to read but not secret)

Caution: the ! function runs with same privilege as user, be careful to trust the source before running this
%run function 
#!  Is called Shebang and tells script to run python 3

```-*- coding: ascii -*- ``` tells script that you are writing in American standard code
Python default is unicode encoding such as utf8
Non unicode : usually only emojis
Recommended to use Visual Studio Code: cross platform Microsoft code editor
Others available such as Spyder, Xcode or Eclipse

Try not to write code in Microsoft Word, pretty unicode punctuation like and instead of ‘ may be changed after pasting, 
Text editors with syntax highlighting: Jupyter, Emacs, Nano, …
With same network connection, you can do collaborative session by sending a link in Visual Studio Code and edit code at the same time

Exercise 2: same as pre-sessional 2.7

Argparse library for parsing
Visual Studio Code: type in terminal box, play run to run code
REST API: work based on web addresses?http-based URLs which respond to requests by returning relevant information 
JSON: data format from JavaScript
PEP-8: Python ENhancement Programme, style guide, provides suggestions for making code better
Code linting; gets rid of excess code and unnecessary examples include: ‘pycodestyl’e, ‘pylint’, ‘pyflakes’/’flake8’ which also looks at bad syntax


General Data Tidyness Points
explicit better than implicit, don’t duplicate functions
Keep things small enough to read in one go
Keep variables meaningful
Simple better than clever
Add comments when they add meaning
Practice the principle of least astonishment (if most people do it this way it’s probably right?)
If working in a group, decide on coding style


Python Modules
Python modules contain code you import into scripts and programs
A Python module is just a text file, don’t put ‘print’ commands in there for example
Perks of using Python modules: often scripts want to do the same thing, to avoid needless code duplication, simpler to update and check 
`import` command uses directories inside `sys.path` variable in order to find files via import command 
`importlib.reload` : tells interpreter to update record of contents of an individual module . Useful during interactive interpreter session if you update code in a module or package.
NB: only updates contents of module passed as argument not module contents imported inside it. If issues, exit and turn it on again
`%reset`: clears every single piece of info out of memory, back to blank slate

Python docstrings
Best way at documenting code
Should start with one line summary 
Docstring should list classes and functions exported by the module with one line summary each

If there are different functions but that use same variables, there will be a clash 
Function should all have docstrings and variable names that make sense
When you’ve tested the code and you find a specific function takes 90% of runtime, it makes sense to rewrite it in a faster and harder to maintain way eg. numpy, numba, cython
Writing your own C extension


 Combined files: file can be both script AND module providing you use a special if test to check how its being used
Specific if format : `if__name__ ==”__main__”:
The code in this block only runs as script (?)

Python Packages: bundle of multiple modules into one place, to make installing and usage easy. Usually consists of python files grouped in a directory tree
Filenames with __init__.py for example is special, and is the module version of the `if__name__` activate if the package is run like python -m mycoolpackage. It usually has import commands to load functions and classes and define some variables
Inside packages, you can have `.import` (the file it is running in), `..import` the file running two level up

**Licenses**
\
UK copyright laws allo creators to control acts of copying, adapting, issuing, renting and lending 
Probably best to use well known and well understood copyright licenses. But a common one is MIT license and it is free. 
Copyright lasts till life of the author + 50-70 years

