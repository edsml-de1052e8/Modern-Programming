# Cheat Sheet
## Python Functions from Class Lectures & Assignements


### NumPy
**Creating 1D arrays**

```a= np.array([-1,0,1])```

or create array using class copy constructor:

```b=np.array(a)```
```print (b)```

Notice the use of square brackets here. Use parentheses to provide a range for the array.

``` a = np.arange(-2,6,2)```
The output here will be [-2 0 2 4] which means that the start point is -2, end point is 6 and 2 is the increment.

```a= np.linspace(-10, 10, 4)``` 
The main difference is that linspace controls the end value and essentially 'forces' the end point to be 10 and provides anything within the provided range and evenly spaced.

``` np.zeros (3)```
Provides 1D array of 3 zeros eg. [0, 0, 0]

``` np.ones(3)```
Provides 1D array of 3 ones eg. [1, 1, 1]

```np.eye (3)```
Provides 3D array of 3 ones but in diagonal! 
[[1, 0, 0],
       [0, 1 , 0],
       [0, 0 , 1]] 


From previously defined array a:
```a.ndim``` : Number of dimensions

```a.shape```: Number of elements in ecah dimension

```a.size```: Total number of elements

```a.dtype```: Data type of each element (64 bit float by default)

These can be called as such:
```print("Dimensions",a.ndim)```

Assigning data type upon creation: ```a= np.array([1.1, 2.2, 3.3], np.float32)``` 
Notice the parenthesis at the end of the data transformation & function ```np.float``` to change to 32 bit float value.

Multi-dimensional array 
``` mat= np.array([[1,2,3],[4,5,6]])``` 2D array

```pprint``` : Pretty print function to have a fancy display of multi-dimensional arrays 

Accessing arrays:
Example array: a[ 0,1,2,3,4,5,6,7]

```a[2:4]``` : Accesses 2nd and 4th value of an array = [2, 3]. Excludes the stop part. eg. a[start:stop:increment]
NB: arrays access starts on 0 not 1!! 

```a[0:7:3]``` Accesses First and second to last value with increment of 3. =[0, 3, 6]

```a[:5:2]``` Accesses first 5 elements of array with increment of 2. [0,2,4]

``` a[5:]``` Accesses last 5 elements of array [6,7]

``` a[1::2]``` Accesses every other element starting at index 1. [1, 3, 5,7]

``` a[-1]``` Accesses all elements except last one.

``` a[::1]``` Prints all elements but reversed. [7,6,5,4,3,2,1,0]

For multi-dimensional arrays:
```a[:3::2]``` : Accesses all rows of a 3 rowed array with every other column. Structure is thus [row, column]

Access using tuple (vs. index notation):

tuple: a[1,0,1] vs index would be a[1][0][1]

Tuple have higher performance.

Slicing: to extract indices, in the form slice(start, stop, step)
``` my_slice= (slice(2, -3, 2))```

```.reshape(3,3```: function to reshape array to 3x3 array

```b= a.copy``` : function to copy arrays, it will be independent of the first array. So no modifications in b will affect array a!

```.reshape``` doesn't change the data, changes shape and size

```a.dot``` : function to multiply vectors and matrices

```np.concatenate``` : function to combine arrays a1 and a2 to a4 array!

```np.random.ranf(10)``` : creates an array of 10 random real numbers

```np.random.randint(0, high=5, size=25).reshape(5,5)``` : creates a 2D array (5x5) reshaped matrix from 1D array of 25 random integers between 0 and 5

```np.random.binomial (5,0.5, size=25)``` : generates random numbers from binomial distribution with 25 numbers.

```np.savetxt('savedata.txt', np.stack((x,y), axis=1), header='DATA', \footer ='END', fmt=%d %1.4f') !cat savedata.txt```

```p=np.loadtxt('savedata.txt')``` reload data to an array

Using the numpy.linalg module: 
import numpy.linalg as la

```n=la.norm(B)```: computes usual quantities and return one of eight normal matrix norms or an infinte number of vector norms

```la.solve(A,B)``` solves linear systems 

```la.det(A)``` : computes the determinant of an array

```A_inv= la.inv(A)```: inverts matrices, though high computational cost

```eival= la.eig(A)```: computes eigen decomposition of a square matrix

```np.power```: raises the first elements of an array to the power of the elements in the second array.

```np.exp```: calculates the exponential of all elements in the array.

**Performance Assessment** 

```import timeit```
```%timeit -n <iteration> -r <repeats> <code_snippet> ```

By default timeit loops over your code 3 times and outputs the best time, also tells how many iterations it ran the code per loop.





