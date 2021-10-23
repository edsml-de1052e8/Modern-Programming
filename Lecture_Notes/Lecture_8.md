# Lecture 8: Continuous Integration



In software development, Continuous Integration (CI) is the practice of developers integrating code into a shared repository several times a day. 
Each 'push' to the repository is then verified by automated testing tools, allowing any problems to be detected early.
All developers merge working copies to a shared mainline several times a day. 

Some CI solutions:
- Jenkis,
- Microsoft Azure Pipelines
- Buildbot
- Github Actions


To begin familiarizing ourselves with Actions, let us dive straight into an example. For this we will make use of a dummy repository located at https://github.com/rhodrin/ci_mpm.
As in the environments lecture last week, start by forking this repository so that you have your own copy within your Github user space. Following this, make a clone of the forked repository

git clone https://github.com/<my username>/ci_mpm.git
  
  - All CI solutions require their own setup.py files which have many concepts but different syntax. For example Azure Pipelines uses a file called azure-pipelines.yml
  
  starts with a ```trigger``` function to start the master function.
  
  - Need to trigger
  - define on what hardware you want to work on the workflow
  - Then Steps to define what the workflow is.
  
  Different syntax between the platforms, although easy to switch between them 
  
  
  
  **Github Actions**
  
  - Relatively new, since 2019, undergoing continuous development 
  - Free
  
  
  
  
  
  Exercise using Test Repo provided:
  
  - After forking repo
  - Local terminal: git clone  (to local repo)
  - ```conda env create -f environment.yml```
  This installs the Anaconda environment file 
  
  NB: Folder .github/workflows/ is a default folder to tell Github that we want to utilise Github Actions for this specific repo using the included yml files.
  
  - A Github runner is a 
  
  
  In Github, on the usual commits/push banner, the green tick means all the pushed changes have passed. 
  When clicking on the Actions tab, you will get further details on these changes 
  
  - Simple.functions.py file: contains @pytest.mark decorator which tells us we want to give several inputs to our test function
  
  The ```on``` segment in a py file, is a segment of the workflow that defines when it will be triggered. eg. a simple ```on -push``` would isntruct the workflow to execute any branch when any push to that branch is made
  
  ```jobs``` is the body of the script: a workflow run is made of one or more jobs. Jobs run in parallel by default. For example a workflow of the form
  
  jobs:
  job1:
  ...
  job2
  ...
   would induce two processes: job1 and job2
  
  
  ```runs-ons: ubuntu-latest``` defines the OS on which the job is run, here it is Ubuntu 
  
  - In Github: in actions tab when the job is done you will get a drop down menu that you can select from
  
  The first step of our job is: the action
  
  ``` - uses: actions/checkout@v2```
  A large range of community developed actions are freely available at the Github marketplace, the ```checkout``` action being used in this first step is simply an action to clone the repository of interest eg. ci_mpm onto the 
github-hosted runner
  
  
Step 2:
  
- ```name``` action logs will appear with given name instead of default one.

  Step 3:
  - ```run``` run commands in the terminal in self-hosted runner you're connected to. ```run: pwd``` to run in public working directory or use ```run | multiple locations```
  
  When looking at the pytest-unit-tests.yml: it has commands to install dependencies such as the requirements or pip upgrades.
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
