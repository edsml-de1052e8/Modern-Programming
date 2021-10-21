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


















