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
  
  
  Within each of the defined jobs is a series of steps that (within a job) will be executed sequentially. A new step is defined via - (which defines the begining of a new step), e.g., - run, - uses or - name. In the absence of name being defined for a step some default naming convention will be used.

**Step 1:**
The first step of our job is

- uses: ```actions/checkout@v2```
This 'uses' is defining a so called 'action' to use (and is where this CI framework derives its name). In Github's own words:

"Actions are the building blocks that power your workflow. A workflow can contain actions created by the community, or you can create your own actions directly within your application's repository."

A large range of community developed actions are freely available at the Github marketplace (which is where all actions used today will come from).

The checkout action being used in this first step is simple an action to clone the repository of interest, ci_mpm, onto the github-hosted runner.

**Step 2:**
  
  
- ```name``` action logs will appear with given name instead of default one.
- name: Set up Python 3.8
  uses: actions/setup-python@v1
  with:
    python-version: 3.8
Notice that this step begins with name. This simply means that in the actions logs this step will appear with the given name (instead of one derived by default). This step makes use of the setup-python action which, as the name suggests, simply sets up the given version of python on the runner (here v3.8). Note that runners will generally have some version of python installed by default but this will be the version 'shipped' with the operating system of choice and possibly not the version you wish to use during testing.

**Step 3:**
- name: Lint with flake8
  run: |
    flake8 .
In the final step we're making use of run. The run command executes the given command-line input in the operating systems default login shell (e.g. bash on unix systems, but note that we can specify any available shell we like using shell: shell_I_want. E.g., to get powershell on a windows machine shell: pwsh).

Single commands can be executed via, e.g.

    run: pwd
Multi-line commands make use of |, e.g.

    run: |
      cd myproject
      python my_sweet_script.py
      echo "my sweet script has run"
In our actual test, we're simply checking that our code is PEP 8 compliant.
  

  - ```run``` run commands in the terminal in self-hosted runner you're connected to. ```run: pwd``` to run in public working directory or use ```run | multiple locations```
  
  When looking at the pytest-unit-tests.yml: it has commands to install dependencies such as the requirements or pip upgrades.
  
  
  
  #### Adding more simple functions: how does ```numpy``` compute pi, sin(x) etc. 
  
  
  First in order to implement these formulas, we'll need to write a factorial function ( or a square root function but using numpy.sqrt) 
  
  To add new file, ```vim filename``` paste the content with the decorator in a new py file when the tab opens and push changes.
  

  ## Additional Github Actions Features
  
```cron jobs```
It is often useful to have workflows trigger on a schedule. Such a schedule can be define using POSIX cron syntax. Take for example the following snippet:

```on:```
 ``` schedule:```
   ``` - cron:  '0 3 11,25 * *' ```
This states that the workflow should be executed at 0 minutes, 3 hours on the 11 and 25 day of every month of every year.
  
  **workflow_dispatch**
Sometimes it's handy to have a 'push button' to run your tests. This is available via the a workflow_dispatch - an example of which is given in the following snippet:

```on:```
  ```workflow_dispatch:```
   ``` inputs:```
     ``` tags:```
       ``` description: 'Run this workflow'```
This introduces a 'Run Workflow' button on the Actions tab under the relevant workflow as shown in the image below
  
  **strategy: fail-fast**
By default, is a job fails the workflow will not progress beyond this job. Sometimes this is not the behavior required. There are a couple keywords available for these that you can find on Github Actions. The fail-fast button is thus set to True. 
  This can be altered by setting the fail-fast flag to false: eg. fail-fast=False

  ```my-job:```
   ``` needs: my-last-job```
  ```  runs-on: ubuntu-latest```

   ```strategy:```
    ```  # Job will run even if its dependency failed```
   ```   fail-fast: false```

   ``` steps:```
   ```   ...```
  
  
 ** Step output's**
  
By default, each step within a job is within a new terminal. If a parameter is not carried on to next step, it is not available (done to avoid conflicts). Sometimes thoguh you want to use the result of one step to add to another. In order to do that you need to define Step outputs. 
  
  A value from one step can be used in a sub-sequent step (if we don't wish to use environment variables) via (e.g. generate some python argument):

  ```  - name: Make some value```
   ```   run: |```
    ```    ...````
    ```    generate some_value```
     ```   ...```
   ```     echo ::set-output name=some_output::some_value```
   ```   id: msv```
```and then```

  ```  - name: Use some value```
     ``` run:```
       ``` python --${{ steps.msv.outputs.some_output }} my_file.py```
  
  Give a name to the output and give it a name to whatever value we want it to take for this new step.
 The id: msv section is a callable id. ```steps.msv.outputs.some_output``` With steps and outputs as the constant and jsut need to change the id and 'some_output' section.
  
  **if statements**
In many workflows we will want some steps to run under one condition and other steps to run under a different one. This can be achieved via if statements. An example is shown below:

   ``` - name: conditional job```
  ```    if: $MY_ENVIRONMENT_VARIABLE == some_value```
     ``` run: |```
  ```      echo "do something"```
Hence the above step would only run is the value of MY_ENVIRONMENT_VARIABLE is equivalent to that of some chosen some_value.

**Matrices**
  
Another immensely useful feature that can be utilized to achieve all kinds of automation. Lets say we want a job to run on several different operating systems and/or with several different versions of python. This could be achieved via the following:

```jobs:
  pytest:
    name: ${{ matrix.name }}
    runs-on: "${{ matrix.os }}"

    env:
      PYTHON_VERSION: "${{ matrix.python-version }}"
      TESTS: "tests/"

    strategy:
      # Prevent all build to stop if a single one fails
      fail-fast: false

      matrix:
        name: [
           python36-ubuntu1804,
           python38-ubuntu2004,
           python37-macOS
        ]
        include:
        - name: python36-ubuntu1804
          python-version: 3.6
          os: ubuntu-18.04

        - name: python38-ubuntu2004
          python-version: 3.8
          os: ubuntu-20.04

        - name: python37-macOs
          python-version: 3.7
          os: macos-latest

    steps:
      ...
  ```
  
  
 How we define these matrices: keyword here is 'matrix' with three names for the python uses. Underneath the 'include' section adds additional parameters
  
  
  
 **Self-hosted runners**
  
Instead of running on the default runners provided, you can also set jobs to be run on self-hosted runners. These could be, e.g., a Microsoft Azure VM or some other bare metal machine. Once the runner is configured, jobs can be sent to this machine via:

runs-on: self-hosted
Note: If you have many different forms of self-hosted runners you can utilize custom 'tags' to send different jobs to different runners, e.g.

runs-on: [self-hosted, gpu]
or

runs-on: [self-hosted, mpi, some_other_tag_if_needed]

  In Github online > Actions > Runners you can add runners and define a job using specific tags to access piece of hardware you want.
  
  
**Github Secrets!**
  
Sometimes a workflow may require the use of sensitive information (e.g. ssh login credentials). Clearly, you don't want such information displayed in a public repository, but if you want contributors to be able to make use of your workflows 'hiding' these is also not an option. In such situations Github Secrets come in handy.

A secret can be set by clicking on the repository setting tab and then under options choosing the secrets tab. They can then be utilized in a worfklow via ${{ secrets.my_secret }} - the value stored can be numerical, a string or characters, a combination or even a snippet of code!
  
Go to Actiond> Secrets. And then creates a repo secret. On any workflow you can then access that secret with the previous syntax  ${{ secrets.my_secret }} which will pull out the code.
  

  
### Some useful actions

  We've already seen the ```checkout``` action in use. Below is an extremely non-exhaustive list of some other useful actions:

**Codecov action:**
  
Codecov was discussed and they have a nice action for uploading and advertising the coverage of your repository:

   ``` - name: Upload coverage to Codecov
      if: matrix.name != 'pytest-docker-py36-gcc-omp'
      uses: codecov/codecov-action@v1.0.6
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
        name: ${{ matrix.name }} 
  ```
  
  
**github-push-action**

  Action to push any changes made by your CI to a designated repository:

    - name: Push new configurations
      uses: ad-m/github-push-action@master
      if: ${{ steps.new-configs.outputs.new_configurations }} == true
      with:
        github_token: ${{ secrets.GITHUB_TOKEN }}

  
  **ssh-action**
  
An action to make login into a machine via ssh and executing some commands/scripts nice and easy:

    - name: start actions runner app
      uses: fifsky/ssh-action@master
      with:
        command: |
          #!/bin/bash
          nohup actions-runner/run.sh >/dev/null 2>&1 &
        host: ${{ steps.host.outputs.action_host }}
        user: ${{ secrets.ADMIN_LOGIN }}
        pass: ${{ secrets.ADMIN_PASSWORD }}
        args: "-tt"```
  
**upload-artifact and download-artifact**
  
"Artifacts allow you to share data between jobs in a workflow and store data once that workflow has completed."

This is incredibly useful when you want to collect and check, e.g., a set of results files from runs on various runners. Make those results files available through artifacts.
  Here are some example snippets of an upload and then a download:
  
```
    - name: Upload result
      uses: actions/upload-artifact@v2
      with:
        name: ${{ matrix.runner }}_${{ matrix.name }}
        path: ${{ steps.fetch-results.outputs.results_file }}
    - uses: actions/download-artifact@v2
      with:
        path: results
  ```
  
  

  
  
  
  
  
  
  
  
  
  
  
  
