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

**Lazy Evaluation**

- concept related to asynhronous computation. Python's default when running through code.

**Threading**

- Fast way of doing parallelism
- The builtin threading module provide basic access to allow general loops and functions to be multithreaded.
- ```threading.Thread```

**locks**
- IO is messed up 
- threads don't wait for each other 
- A lock is effectively a token that only a limited number of threads (often 1) can hold at a time. 
- If the thread can't pick up the token, then it does nothing and waits for a bit to try again. This sacrifices efficiency for safety.

**Python Global Interpreter Lock (GIL)**

- So far we've always been speeding up a do nothing function using time.sleep. This is a reasonable model for basic IO processes. 
- What happens if we try to do something useful instead? Maybe we'll start off with something in numpy?

- For thread safety and to maximise speed, Python code usually runs one step at a time. So except for specific problems eg. numpy, pandas. GUIs, threads aren't always the answer.
- Not for general python calculations


**Multiprocessing**

- So, what's the solution to make Python code fast in parallel? 
- The multiprocessing module implements process based parallelism for Python problems, and since these are separate processes, they each have their own GIL.
- import multiprocessing
- Got a lot of helper functions
```pool = multiprocessing.Pool(processes=4)```
```y = pool.map(expensive_func, a)```

- Note that we have to use a function which can be serialised to pass to other functions, and the easy way to ensure that is to write it in a module.


# Dask

- In this section we parallelize simple for-loop style code with Dask and dask.delayed. - - Often, this is the only function that you will need to convert functions for use with Dask.

**Parallelize with dask.delayed decorator**

- When we call the delayed version by passing the arguments, exactly as before, but the original function isn't actually called yet - which is why the cell execution finishes very quickly. 
- Instead, a delayed object is made, which keeps track of the function to call and the arguments to pass to it.
- The z object is a lazy Delayed object. This object holds everything we need to compute the final result, including references to all of the functions that are required and their inputs and relationship to one-another. 
- We can evaluate the result with .compute() as above or we can visualize the task graph for this value with .visualize().


**Example: Parallelizing a Pandas Groupby Reduction**

- Here we read several CSV files and perform a groupby operation in parallel. We are given sequential code to do this and parallelize it with dask.delayed.

- The computation we will parallelize is to compute the mean departure delay per airport from some historical flight data. 
- We will do this by using dask.delayed together with pandas.

**Sequential code**

- The above cell computes the mean departure delay per-airport for one year. 
- Here we expand that to all years using a sequential for lfrom glob import glob
```filenames = sorted(glob(os.path.join('data', 'nycflights', '*.csv'))).```


- We can use dask.delayed to parallelize the code above. Some extra things you will need to know.

1. Methods and attribute access on delayed objects work automatically, so if you have a delayed object you can perform normal arithmetic, slicing, and method calls on it and it will produce the correct delayed calls.


2. Calling the .compute() method works well when you have a single output. When you have multiple outputs you might want to use the dask.compute function:

>>> from dask import compute
>>> x = delayed(np.arange)(10)
>>> y = x ** 2
>>> min_, max_ = compute(y.min(), y.max())
>>> min_, max_
(0, 81)
This way Dask can share the intermediate values (like y = x**2)

So your goal is to parallelize the code above (which has been copied below) using dask.delayed. You may also want to visualize a bit of the computation to see if you're doing it correctly. See the exercise notebook for where to start.






















