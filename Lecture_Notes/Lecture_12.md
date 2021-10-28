# Lecture 12: Parallel Computation

## Setting up Dask

In lecture 12 directory run:

conda env create -f environment.yml


**What is Parallel computation?**

In the simplest sense, parallel computing is the simultaneous use of multiple compute resources to solve a computational problem:

A problem is broken into discrete parts that can be solved concurrently Each part is further broken down to a series of instructions Instructions from each part execute simultaneously on different processors. 
An overall control/coordination mechanism is employed.
A metaphor for this would be an orchestra with a musician playing a note ir multiple musicians playing one note each.

Similarly, to perform a parallel task on a modern computer, one could have a single instance of a program do many things at once, or have many copies of a program do one thing each. 
In more exact language, task parallelism on a multi-processor computing system can be multi-threaded or multi-process.

**Bubble sort**

- simple to understand but not so fast sorting algorithm
- run through the array (left to right), compare pair of elements, swap them if they're wrong order
- first run finds max/min
- start again on n-1 element which might still be wrong



**Threads**

- Cheap to create and destroy
- Running within the program itself, sharing data with program memory
- Can't have two threads sharing same thing at the same time, need to control which one acts on which resource using 'locks'
- Limited to one computer
- Basically what your web browser does

**Processes**

- Higher overhead to fork process
- have own copy of resources
- communicate thru network 
- can be distributed across multiple machines
- Break array down in different pieces which communicate together
- what many HPC programs fo a lot

**Writing parallel algorithms**

- Not all problems parallelize easily. if each step in a problem depends explictly and nonlinearly on the one before, then it is likely to be hard to divide the workload.
- Similarly, some problems are "embarrassingly parallel", where a single set of operations needs to be performed on all the elements of an array of data.
- This is precisely the sort of problem which is well suited to pass to a GPU hardware accelerator, and which often occurs in graphics processing and linear algebra.
- simplest algorithm would be:
``` for x in x:```
```f(x)```

**Synchronous vs. Asynchronous**

- Similar to parallel in appearance. 
- synchronous: when you sit and wait for results eg. using the ```time.sleep function```
- asynchronous: a unit of work is allowed to run separately from the primary application thread. 
Doing one function then waiting and meanwhile does another function. eg, using the ```await asyncio``` command.
```async.gather``` puts results in a list (?)



Modern Python 3 contains an async keyword, to declare a function as asyncronous, and an await keyword to make a call block and wait to collect the final results. 
Can't run it without that keyword.
A useful builtin module, asyncio, gives us some more control over the running of these processes. Let's start by defining some asyncronous functions (also called "coroutines").

In general, this sort of issue tends to be linked to IO, where the process involved is slow (e.g. it waits tor something, or communicates across a network.

Asynchronous routines are:
- not usually default
- hard to get right, surprising (can show weird connections between codes)
- Hard to debug, parallel is hard to debug but this is worse
- can sometimes really decrease running time

To recap, use async:
- When problem is I/o bounded (waits on non-Python)
- I/O is slow (web communication for example)

















