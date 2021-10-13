# Lecture 3: Environments


Environment variable: 

Why do we need a virtual environment
- Tool to help keep dependecies required by different projects separate by creating isolated python virtual environments for them.
- For testing software, 


- By default every project on your system will use the same directories to store and retrieve site packages

Environment examples
- venv: inbuilt library in Python 
--> how to create environment in lecture 3, on Mac with Python 2 and 3 type in `python3` in Virtual Studio Code
- virtualenv: older than venv, good for testing and benchmarking
- docker: environment to create containers to isolate packages. Good for testing software packages and cross operating system compatibility. Although for software development, tools like Anaconda are more convenient.

**Anaconda**
- Open source distribution of Python, so doesn't use Python. It simplifies package management. Comes with apps such as Jupyter Notebooks, Conda environment manager and Pip for package installation and others such as matplotlib, NumPy, ...
NB: many Anaconda tutorials online

In Virtual Code:
- when repository is forked and cloned (using Terminal or VSCode), the file 'environemnt.yml' has a breakdown of channels and the dependencies


**General note on Git:**

-> see lecture 3: step by step version control from Terminal or VS Code to Github
- convention to name package with easy to remember names
- From class repo -> clone and don't forget to fork 
- Fork: creates a copy of a repository (so you don't commit/push to public repo and amend it, instead of doing it locally)
