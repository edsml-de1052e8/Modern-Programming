## Lecture 1: Introduction to Modern Programming & SciPy
***Monday October 2021***




Supplementary reading:
Optional! 

General Info:
You will however get good marks if you do all the exercises 
Lectures in the morning, complete the exercises in the afternoon and aim to be done at the end of the day
Assessment released on Tuesday and released Friday at 4pm 
Go through lectures for couple mins maybe before lecture




---
SciPy General Lecture Info

Learn what NumPy arrays are
Basic array manipulations
Vectorial code
sciPy
2D plot
Combining plots

Reading:
Nature paper


SciPy: ecosystem of  open source software which includes: 
NumPy
Matplotlib
Pandas 
Sympy 
It supports multidimensional arrays, matrices, linear algebra operations, random number transformation, Fourier transforms, polynomials etc

Pybrt 
Used to get feedback on repetitive problems 
Copy constructor: ```b= np.array (a)
Print (b)```

Use ‘type’ function to check what kind of data you are dealing with eg. float, string

Key array attributes
A.shape
Ndim functions

Multidimensional array: basically a list of list eg. ```np.array([1, 5,6],
[4,5,6])```


Vectorisation reduces running time and helps you avoid using -for loops
It also works with functions 

NB: don’t write stuff from first principle, make it spicy

Write code in the most convenient manner, use functions to figure out the performance of your code and measure running time:

Use function %timeit


#### SciPy: Highlights

Sometimes packages are already created for the purpose of the things you want to achieve
For example you don’t have to write your own integration, can use multiple functions like ‘integrate’
Same goes for optimisation 
Matplotlib package within SciPy: mainly for 2D plots
import matplotlib.pyplot as plt
NB: avoid using import *
Don’t forget to use axis labelling 
Save plot in picture format: plt.save g("out.png")
Widgets are useful but don’t spend too much time on it, ‘black hole for your time’

##### Summary

NumPy: defines nd.array which is an efficient structure for large arrays, matrices and tensors, and functions to manipulate them
SciPy: defines a lot of user-friendly routines useful for scientific codes
Both rely on efficient low level code, and will generally be much faster than if you try to re-implement them yourself
Vectorization !
Matplotlib: allows you to draw and save plots, from the simplest 2D line plot to complicated 3D plots.
Refer to online documentation for a complete list of features: https://docs.scipy.org/doc/

