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


First, lets check the status of our repository and make sure we add any new files:
git status
will return something along the lines of ```bash On branch master Your branch is up-to-date with 'origin/master'.
Changes not staged for commit: (use "git add

Untracked files: (use "git add

The import untracked file we need to add is `scripts/solve_matrix_equation.py` - the others are meta-data **we do not want** under version control. We can add it through
```bash```

```git add scripts/solve_matrix_equation.py```

Next, commit the changes we've made via

```git commit -a -m "<my commit message>"```

```git add scripts/my_new_script.py```

followed by

```git commit -a -m "<my commit message>"```

Push these changes to github

```git push```
```git push -u origin lecture```










- convention to name package with easy to remember names
- From class repo -> clone and don't forget to fork 
- Fork: creates a copy of a repository (so you don't commit/push to public repo and amend it, instead of doing it locally)


As a final note, think about why is it important to have both environment.yml and requirements.txt files.

The environment.yml was used only when creating our environment. Remember it was useful to have the requirements.txt file to install the required packages when developing our environment. (Although we could have also continuously updated our environment file and then updated our environment via conda env update -f environment.yml).
In any case, we generally want both for people making use of our package who are not using Anaconda. As we saw earlier, we could use such a requirements file in venv.

Additionally, what if we want some packages to not be installed automatically when creating our environment? For various reasons, we may with to have an, e.g. requirements-optional.txt file present (generally the packages listed in environment.yml and requirements.txt should be in sync unless there's a good reason for them not to be). Any such optional requirements can be installed via the pip install -r ... .txt command once again.
