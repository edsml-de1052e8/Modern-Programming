# Lecture 10: Debugging

We all, even the great Fabio Luporini, write buggy code. Write your code with testing and debugging in mind.
- Keep It Simple, Stupid (KISS):
What is the simplest thing that could possibly work?
- Don't Repeat Yourself (DRY):
- Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
Constants, algorithms, etc.
- Try to limit interdependencies of your code. (Loose Coupling).
- Give your variables, functions and modules meaningful names (not cryptic/mathematics names).


**The world’s first computer bug?**

On September 9th, 1947 at 3:45 p.m., Grace Murray Hopper logged in her log book the first computer bug! Her log read: 
"First actual case of bug being found". 
The term "bug" in computer science is now, of course, not taken literally. 
It is used to describe a flaw or failure in a computer program that causes it to produce an unexpected result or crash.

**Mandelbug**
Mandelbugs do not change their properties or vanish like Heisenbugs. Instead, they are so unusual and complex that there is typically no practical solution to fix them. In fact, Mandelbugs may be so nondeterministic that many scholarly developers believe that fractal mathematics inventor Benoit Mandelbrot developed the Mandelbug to drive developers insane.

**Bohrbug**
A software bug which manifests reliably under a well-defined, but possibly unknown, set of conditions.

**Schroedinbug**
A software bug which manifests only when somebody debugging it finds out that it shouldn't work at all.


**Pyflakes: fast static analysis

Out of analysis tools such as pylint, pychecker, etc pyflakes is a fast and simple option. 
Good for detecting syntax errors, missing imports, typos, ... 

**Debugging workflow**

For debugging a given problem, the favorable situation is when the problem is isolated in a small number of lines of code, outside framework or application code, with short modify-run-fail cycles

- Make it fail reliably. Find a test case that makes the code fail (in the same way) every time.
- Divide and Conquer. Once you have a failing test case, isolate the failing code.
Which module.
Which function.
Which line of code.
=> isolate a small reproducible failure: a test case/minimum failing example

- Change one thing at a time and re-run the failing test case.
- Use the debugger to understand what is going wrong.
- Take notes and be patient. It may take a while.

Note: Once you have gone through this process: isolated a tight piece of code reproducing the bug and fix the bug using this piece of code, add the corresponding code to your test suite.

**Minimum Failing Examples (MFE)**

Given the occurrence of a particular bug, a minimum failing example (MFE) is the simplest piece of code that can reproduce an instance of the particular bug in question (which was probably discovered through building a larger more complex script).

When approaching someone for help debugging a problem, it is considered good practice to provide them with an MFE. This will often drastically reduce the time taken for them to debug the problem. 
Further, when contributing to an open source project and reporting a problem (e.g. opening a bug report issue on Github), the developers will frequently ask 'Please could you provide an MFE'.

**Using the Python Debugger**

The python debugger, pdb: https://docs.python.org/library/pdb.html, allows you to inspect your code interactively.

Specifically it allows you to:

- View the source code.
- Walk up and down the call stack.
- Inspect values of variables.
- Modify values of variables.
- Set breakpoints.

Ways to launch the debugger:

1. Postmortem, launch debugger after module errors.
2. Launch the module with the debugger.
3. Call the debugger inside the module


Postmortem
Example 1: You're working in ```IPython``` and you get a traceback.

Here we debug the file index_error.py. When running it, an IndexError is raised. Type %debug and drop into the debugger.



Example 2: Post-mortem debugging without IPython

In some situations you cannot use IPython, for instance to debug a script that wants to be called from the command line. In this case, you can call the script with ```python -m pdb script.py```:

**Step-by-step execution**

Example: You believe a bug exists in a module but are not sure where.

For instance we are trying to debug wiener_filtering.py. Indeed the code runs, but the filtering does not work well.

Run the script in IPython with the debugger using ```%run -d wiener_filtering.py``` :
Set a break point at line 34 using b 34:
Continue execution to next breakpoint with c(ont(inue)):


**Other ways of starting a debugger**

Raising an exception as a poor man's break point
If you find it tedious to note the line number to set a break point, you can simply raise an exception at the point that you want to inspect and use IPython’s %debug. Note that in this case you cannot step or continue the execution.

**Debugging test failures in pytest's**

You can run, e.g., ```pytest --pdb my_test.py``` to drop in post-mortem debugging on exceptions, and ```pytest --pdb-failure``` to inspect test failures using the debugger.

This is useful since, owing to the manner in which pytest works, we can not from ```IPyton embed; embed()``` to drop into a test (without messing around more than we'd like).

Calling the debugger explicitly
Insert the following line where you want to drop in the debugger:

```import pdb; pdb.set_trace()```

**Debugger commands and interaction**

NB: Debugger commands are not Python code.
You cannot name the variables the way you want. 
For instance, you cannot override the variables in the current frame with the same name: use different names than your local variable when typing code in the debugger. 
Not this is different from dropping into embedded IPython where you can override existing variables.


**Debugging segmentation faults using gdb**

Segmentation faults: memory access error usually. 

If you have a segmentation fault, you cannot debug it with pdb, as it crashes the Python interpreter before it can drop in the debugger. Similarly, if you have a bug in C code embedded in Python, pdb is useless. For this we turn to the gnu debugger, gdb, available on Linux, MacOS and Windows.

Note:

There are many ways in which gdb can be installed, but among the simplest is through Anaconda. From within a suitable enviroment it can be installed via conda install -c conda-forge gdb. Then type gdb --version to check it has installed correctly. The main branch of gdb does not appear to support the new Mac M1 chips and hence we're going to log into a Ubuntu machine to demonstate it's use.

WARNING: gdb can be fiddly to set up: don't waste too much time on the example below unless your super-keen to get it running right away. pdb will be sufficient for the assessment this week.


Before we start with gdb, let us add a few Python-specific tools to it. For this we add a few macros to our ~/.gdbinit. The optimal choice of macro depends on your Python version and your gdb version. A simplified version has been added in .gdbinit located in the files folder, but feel free to read DebuggingWithGdb.

Some of the paths specified in .gdbinit provided are specific to my machine. You'll need to modify these.

For a list of Python-specific commands defined in the .gdbinit, read the source of this file.

To debug with gdb the Python script segfault.py we start gdb via

```gdb --args python```

Gdb is very versatile, can use with C and C++ for example. 


### Debugging distributed (e.g. MPI) computations

Later in this course you will encounter the ```mpi4py```

(https://mpi4py.readthedocs.io/en/stable/) package. Debugging MPI based programs can be a real pain and tools such as `pdb` are often less useful. Utilising manual debugging techniques in tandem with tools such as [tmpi](https://github.com/Azrael3000/tmpi) can however be an effective method.



















