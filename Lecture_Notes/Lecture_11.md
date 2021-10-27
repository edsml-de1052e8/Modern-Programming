# Lecture 11: Profiling & Optimisation 


When to optimise?

- Make it work: write the code in a simple, readable, and maintainable way.
- Make it reliable: write tests and make sure that if we break the code, the tests will let us know
- Measure, measure, measure: Measure the performance, do not guess!
- Convince ourselves that our code is too slow: Does it hurt if it runs too slow?
- Consider the costs of optimisation: Hardware is cheaper than the developer time.
- Optimise until the code is fast enough and not as fast as possible.


**Profiling**

- TRying to find bottlenecks in order to improve the code and increase performance.
- Profiling allows us to measure resources (CPU, RAM, disk I/O, network I/O, etc.) used by our code.
- We want to identify code segment that requires least amount of work but will result in largest performance gains.
- Always measure, do not guess.
- Profiling adds an overhead - slows our code even further (10, 100 times)
isolate a piece of code you want to profile (importance of modular design). By measuring how much resources the code is using, we are slowing it down. 
- Execution time always varies
- In the background, your computer will perform different tasks using resources.
do not attribute an improvement to a random variation in execution time

**Measuring Time**

- Using ```time``` module: standard Python library. 
A very simple approach could be using ```time.time().```
We measure time before we start our calculation (start) and as soon as we finish (end).
Execution time is the difference between end and start. So you run start before the line and end after one line.

Ex:

```import time```

```start = time.time()```
```sum_1_to_n(n=100_000_000)```
```end = time.time()```

```execution_time = end - start```

```print(f'The execution time was: {execution_time} seconds.')```

NB: be aware of randomness, time might change a bit between each run.

**Writing our decorator** 

- A decorator is a function that takes another function/class and extends its behavior.
- Take a function (eg. 'notification'), pass it, if it is a function then you can just call it such that: eg. ```func()```


def notifications(func):

    def closure():
        print("Get ready...")
        func()
        print("Done.")
    return closure

def say_whee():
    print("Whee!")

say_whee_with_notifications = notifications(say_whee)

say_whee_with_notifications()

- Another way to do it is with the @ function which calls the previous function.


def notifications(func):
    def closure():
        print("Get ready...")
        func()
        print("Done.")
    return closure

@notifications
def say_whee():
    print("Whee!")

say_whee()


**Simple Timing Decorator**

- Decorator function to compute time between each line of code.

def measure_time(func):

    def closure(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f'The execution time was: {end-start} seconds.')
    return closure

@measure_time
def sum_1_to_n(n):
    s = 0
    for i in range(1, n+1):
        s += i
        
    return s

sum_1_to_n(100_000_000)


**Timeit**

- Part of the Python standard library (available everywhere and we do not need to install it)
- Provides a simple and quick way to time small bits of code
- Command-Line, Python, and "magic" IPython interface
- More information: https://docs.python.org/3/library/timeit.html


**Measuring Command-Line Interface (CLI)**

- Run it in Terminal:

```$ python3 -m timeit -n N -r R "statement"```

- Although execution time will vary between each measurmenet. A way to go around it is to run it in a loop. Here you run the object N, R times. In the end it will choose the best time as the result.

Example in Bash Command (defined by ! exclamation point), with 1+2 the simple function/ statement to be measured.
```!python3 -m timeit -n 1000 -r 10 "1 + 2" ``` 

However if you run just a ```time.timeit('2+3')```, you have to specify how many loops it does, otherwise computation time is too long. By default, timeit takes 1 Million loops as a number R .


**%timeit mangic**

- This is different as it gives the mean and standard deviation, not the best time like in timeit.py.
- Both methods have their advantages and disadvantages.
- Use one method or the other - do not mix them.

Ex: ```%timeit 1 + 2  # notice the cell execution time```

7.75 ns ± 0.0314 ns per loop (mean ± std. dev. of 7 runs, 100000000 loops each)

This command was run 100 Million times. 

- We should pay attention to standard deviation - if it it too large, we might want to repeat the measurement.
- The command 1 + 2 was executed in r runs, each consisting of n loops (r * n in total) to get the statistics.
- We can specify the numner of runs (-r) and the number of iterations (-n).

**%timeit on entire cell**

- You add double %%
- such that ```%%timeit setup```
- It changes the r and n depending on the input.

NB: don't measure the timeit of the import, put it after imports.

**%timeit ouput object**

- Instead of printing the result, we can obtain the output object.
- ```%timeit -o a**2```
with -o (prints output object)

- Can place it in a variable: ```%timeit -o a**2```

Can also get the measured times of individual runs: 
```timeit_object.timings```

Can also get stats such as average or worst time:

timeit_object.average
timeit_object.best
timeit_object.worst
timeit_object.stdev


**cProfile**

- So far, we measured total CPU time.
- How do we find a bottleneck? Where does our code spend most time?
- cProfile helps us understand which functions take most CPU time.
- Part of the Python standard library (available everywhere and we do not need to install it)
- It gives us more information, but adds extra overhead, it slows our code more.

The use of the underscore _ in a function, is when you don't need the variable. 
random.random gives a float between 0 and 1

def random_list(n):
    res = []
    for _ in range(n):
        res.append(2*random.random() - 1)
        
    return res


- Create profiler object:
profiler = cProfile.Profile()
profiler.runcall(estimate_pi, n=1_000_000)
profiler.print_stats()

- with estimate_pi is a function name
- n: number of iterations

- The print_stats: shows table with multiple times.
- Percall: is time spent by each line as you run it .
- Cumtime: when you add all the lines up together line by line

- Can save those stats and put them in a file using:
```filename = 'stats.prof'```

```profiler.dump_stats(filename)```

!ls stats.prof  is used to print the file

**Visualising cProfile results**

- can use snakeviz to visualise and better understand the results, it opens up a tab in your browser.
- If you move the cursor above the squares that pop up then you can get the info on stats
- pip install snakeviz  to add the snakeviz package.

In Terminal/Command Line:
```$ snakeviz "stats.prof" &```


**%prun magic**

- Similar to timeit, we can run profiler using a magic command %prun.

**Exercise 2**

- introduces function: ```time.sleep(0.01)``` so function sleeps for 0.01 seconds.
- each time function fact_sum_list is called you add the fast_sum function that puts it to sleep for 0.01 s. 

**line_profiler**

- cProfile told us what function "eats" most resources.
- To investigate further, we should measure how much CPU time was each line of the code uses.
- For that, we use ```line_profiler``` by Robert Kern.
- You can install it by running pip install line_profiler
- In .py file, we decorate functions we want to inspect with @profile.

Go to python notebook and add: 
```!kernprof -l -v filename.py```after your function.

- Gives back % Time: amount of time (in percentage) spent by each of these lines. 

### Optimisation 

**General gudelines**

1. Convince yourself that your program is too slow.
Does it hurt if the program runs slowly?
Is it slow for a realistic use case (on a case you are applying it to not simple things like 1 or 2)?
Are there any external causes (network, IO, ...)
Find bottlenecks by (line) profiling - measure, don't guess!
One accurate measurement is worth a thousand expert opinions. - Grace Hopper

2. Optimisation costs.
Optimisation is time consuming.
How much readibility and maintainability will suffer?
Is it cheaper to use better hardware (hardware is cheaper than the developer time).

3. Do not optimize while you develop
Correct first, fast later.

4. Always check the result of optimisation (unit tests, coverage)


- Function 'sets': 
``` def using_sets(x, y):```
```    return list(set(x) & set(y))```

It is a built-in parameter that can prevent you from using for loops and is good for reducing time. This finds the common point in the two lists x and y. 


**Ex 2: Matrix-Matrix multiplication**

A = np.random.rand(100, 100)
B = np.random.rand(100, 100)

```def matmult_numpy(A, B):```
  ```  return A @ B  # np.matmult(A, B)```

```assert np.allclose(matmult_loops(A, B), A @ B)```

Ex3: Can use cache to save results of previous calls 
Each time you want to compute it you read the table called functools from standard library.

eg. 
```import functools```

```@functools.cache```
```def fibonacci(n):```
```    if n == 0:  # There is no 0'th number```
```        return 0```
```    elif n == 1:  # We define the first number as 1```
```        return 1```
```    return fibonacci(n-1) + fibonacci(n-2)```

NB: Caching is good for ingers, Fibonnaci etc. Not so good for floats because of round errors. 



















