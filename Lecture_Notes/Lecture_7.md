# Lecture 7: The Cloud part II, Virtualisation

- It's /data/json which should accept POST requests

- Result should be dateTime and the output format should be Data Frame

**Emulation**

Emulation: computer software acts as a function on hardware, taking in inputs and providing an output. eg. blinking, storing files 
It can also run on another piece of hardware, when processed appropriately.

Software written for one set of hardware can run on another if the inputs are the same and the outputs are processed appropriately.
Those inputs can be provided by hardware or software 

Examples:
Old computer consoles
Rosetta on M1 Macs

**Translation layers**
- Rather than faking hardware, it fakes software.
- Take user calls out to one operating system & run them on another Examples:
WINE on Linux runs windows software
WSL on Windows (particularly the first version

**Virtual Machines**
- As well as faking other hardware, computers can fake being (subset of) themselves.
- Second "layer" of file system, OS kernel & userspace on top of original, rather than BIOS
- Kernel: is the part of the system that interacts with the hardware (?)

- Virtual machine Examples:
Virtual box, WSL 2 (kind of) VMware

- Virtualization is popular in data centres. So you have server mother boards with server chips on them.

- Server chips: have slow clock speeds (vs desktops) but have large core counts (up to order 50). You want tasks to run in parallel.
- Virtualization puts many computers on one chip.


Concrete Example: Buying time on Azure Virtual Machine

- In Azure -> Virtual Machine -> create 
- Resurce group is a bundle of things and allows you to delete it straight after being done with using it.
- When choosing instance region: bear in mind the features available from data centre, the cost and rapidity (closer the faster but also depends bc v good in the US)
- Image: picks what software you will be using, what more to install etc.
- Size: where you can select what size of virtual machine you want, how many cpus, etc.

After creation: there is a public IP address that I will be "talking to" .

In command line: will ask for password (the one created for the VM).
- run command 'ls' to see what is on the machine. 
- Make a test file: 'echo "This is a test." >test.txt

``` -m http.server --port 80 ```
if error message: you have to connect as admin so add 'sudo'
```sudo -m http.server --port 80```


To delete the virtual machine:
- Go to resource group and delete it from here: here it doesn't take away everything like your adaptor?
- Type the resource group name: delete the VM, the Disk .

- Remember machines are cost and credit!

* Azure Web Services*
- Relevant protocols for Azure:

- Remote Desktop Protocol (RDP), to access Windows (and some linux) virtual machines and to use them in the same manner as a desktop.
- Secure Shell (SSH), to access a terminal on VMs (or apps on linux through X forwarding)
- Hypertext Transfer Protocol (HTTP/HTTPS) to access services via the web, whether through a browser, or another application.

- RDP: The remote desktop protocol (RDP) connects to a remote Windows machine like it's on your desk.

Available for:

Windows PC
Linux
Mac
Android
iOS

- SSH - secure shell: Cryptographically secured shell (i.e. prompt/terminal/command line interface) c. Available for (virtually) all systems.
Most usual way to connect to large HPC systems. Widely used, cheap to run, easy to leverage.

- Public key cryptography - based on idea that some things are hard to "undo" without secret information - many different algorithms - publish some information- - keep some secret


- RSA algorithm
Pick two largish primes ( $p$ & $q) and one integer $e$).
Find second integer $d$ with$$ e\cdot d = 1 \mod (p-1)(q-1) $$
a couple of extra constrainsts, but nothing
all (relatively) cheap to do.

- Command in the form ssh <user>@<server name> connects to remote computer as specified user using port 22.

Firewalls tend to block unexpected connections. Usually in the form of two identification systems. SSH needs to be enabled on the computer.

E.g ssh jrper@sshgw.ic.ac.uk connects me to the college gateway server.



  
  **Microsoft Web Site**
  
- Creating an app
 - Name is quite important, it will be the name in your URL: eg. flaskExample
 - Publish section: Can either publish using code or a Docker container
 - Runtime stack: software eg. Python 3.8
 - Pick the region: eg. US
 - App Service Plan: Linux plan, jrper_asp_Linux_centralus
 - Also option to link with Github
  
  Create Web App
  
  
  ••Containers**
  
- lightweight form of virtualization, in a case  you can run same operating system kernel with many userspaces and filesystems
A lot less work means can run more containers on the same machine. So rather than running VM with 25 cpus/50 you can run 15/50 cpus on the same hardware.

  - Docker: Most famous & widely used container system is Docker.
Usually used for small linux containers.
 
  Terminology: scripts are called Dockerfiles
  - build bundles are called images, containing a frozen system, you cn then unfreeze those systems and then run bundle as a container

  Dockerfile
  
  -> code below is not terminal, it is in docker filing system not your computer!!!

```# set base image to build on```
```FROM python:3.8```

```# set/create current working directory inside container```
```WORKDIR /example```

# copy a file from the host to the container
```COPY requirements.txt```

# run a shell command
```RUN pip install -r requirements.txt```

# default command to run when container starts
```ENTRYPOINT python```
  
**General Note:**
 - RUN command: runs instruction in that image to install requirements
 - ENTRYPOINT: sets default command when docker command is run
  
  
Build Dockerfile into image with:

```docker build [OPTIONS] PATH```
e.g. inside the directory containing the Dockerfile and requirements.txt file.

```docker build --tag example .```
Start container from image with using the 'tag' function

```docker run [OPTIONS] IMAGE [COMMAND]```
eg.

```docker run -it example```
or, for a shell

```docker run -it example bash```
  
- Images can be uploaded to Dockerhub. So can upload an entire computer. Bypasses issues due to differences in your local computers, makes sure everything works. 

Need to upload to Github first (?)

 
  **Local Python GUIs**
 - Number GUI tools
  
  ### Local Python GUIs Number GUI Toolkits compatible with Python, including: - [TK](https://docs.python.org/3/library/tk.html), - [GTK+](https://python-gtk-3-tutorial.readthedocs.io/en/latest/) - [QT5](https://www.riverbankcomputing.com/static/Docs/PyQt5/). Last one works well with Anaconda
  
The _mygui.py_ script needs the `qtpy` package. ```bash pip install qtpy ``` - Note this is built to work locally, not on Jupyterhub/via Flask. - Need to use the `%gui qt` iPython magic in Jupyter. - Other toolkits exist.
  
  - GUI only works on local system or web interface, doesn't work via Jupyter Hub or via Flask
  
**Security and the Cloud**
  
  - Expect to be attacked
  - Network firewalls limit access to expected protocols from expected IPs (limit Azure from ICL account)
  
Azure provides controls on network interfaces to limit the ports and services over the network. Default (and safest) option denies access unless you ask for it.
  
  *Authentication & Authorization**
  
  - Authentication: proving it is you
  - Authorization: allowing access to
 
  In general:
  - use https instead of http
  - add a "salt" to the password eg. unique piece of information 
  - Hash your password
  - Store the salt & hashed password with you immutable user key  in your database
  - so when user logs in apply the same algorith and compare results, -> look up user, add salt and hash
  - best practice is to say "something has gone wrong" instead of letting ppl know if username or password is correct
  - regardless secure your database and only grant access on a need to know basis
 
  **Single Sign On**
  
  - Also known as SSO, complicated, both for you and user, SSO does this using tokens (short lived long passwword through trusted 3rd party. 
  Many providers: Google, Facebook, Twitter, Weibo

  Many of these use a common framework called Open Authentication version 2 (also known as OAuth2).

A variety of SSO helper packages exist for Python. For Azure & Microsoft Active directory, the relevant package is called msal. For (most of) an example use case, leveraging another package called flask-login look at the files in the examples/auth directory.

login.py
_teams.py


The msal package is the easiest one. Example: look at 'simple' file in Lecure 7
  
  GDPR & Legal requirements
  - try not to store personal info
  - Individuals have the right to request copy of records 

  ** Other Azure Cloud Services**
  
  Azure Functions
- Azure Functions is a service which allows a Python function to be accessed directly from the web via parameters passed through a URL. An example will be shown in the lecture.

Azure has several systems available to store data, depending on its format. Might be:

unstructured binary data,
structured databases (or spreadsheets)
or something in between.
  
  - Blob Storage: can store binary data and store it on other system. o quote Microsoft, blob storage is designed to hold:

Serving images or documents directly to a browser.
Storing files for distributed access.
Streaming video and audio.
Writing to log files.
Storing data for backup and restore, disaster recovery, and archiving.
Storing data for analysis by an on-premises or Azure-hosted service.
-Data is accessed via a network interface,

You pay for it!
Charges depending on:
how frequent access is
the volume of data transferred.
In general a URL is assigned to each item, which can be used in multiple ways, including those listed above, to access the blob object.
  
  
  ** SQL**

- SQL: Azure provides a number of ways to access data in databases.

Most of them are built around the SQL database language:

From 1974
hierarchical approach (here top-down):
- database server holds databases,
- databases hold tables,
- tables hold records
- records have multiple values in multiple columns.
  
  
Python comes with inbuilt support for SQL in SQLite format, in which individual databases are stored in local files, via the builtin package sqlite3. To use a full fat SQL server on Azure appropriate additional software should be downloaded e.g the MySql connector. However the basic syntax to connect to, read and update individual databases remains similar.
  
  - SQL: users can work at same time, changes get updated before each amend so less conflict issues compared to Git

```import sqlite3```

```#Connect to/create db file
conn = sqlite3.connect('my_db.sqlite')
cur = conn.cursor()```

  ```try:
    cur.execute("CREATE TABLE fruit(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), price INTEGER)")
    print("Table created")
except sqlite3.OperationalError:
    print("Table exists")

# Write some data
cur.execute("INSERT INTO fruit (name, price) VALUES (?,?);", ("apple", 300))

# Read some data
cur.execute("SELECT * FROM fruit;")
rows = cur.fetchall()

for row in rows:
    print(row)

  
cur.execute("SELECT price FROM fruit WHERE id=?;", "1")
row = cur.fetchone()
print('Price:', row)

conn.commit()
cur.close()
conn.close()```
  
  - As a general note, in SQL: commands are in capital.
  - Power of SQL, a bit like pandas, is that you can select a specific value from a column with specific criterias! eg. ```SELECT price FROM fruit WHERE id=?;", "1"```
  
  
  For complicated interactions use Pandas or SQLAI
  
  
**Azure ML Service**
This product provides a service somewhere between PaaS and SaaS allowing you to develop black box machine learning solutions in classification and prediction. To understand what's going on, you should probably wait until later in the course, but feel free to study independently.






