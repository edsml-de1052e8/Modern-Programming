# Lecture 9: Representation of real numbers


Representation of real numbers
Every real number $x \in \mathbb{R}$ is a point on the real axis.

### Exercise 1:

bianry number -> if "string" has a point (so it is decimal) then return the decimal equivalent. Otherwise return False 

**General base-B expression**


```For $\beta &gt; 10$, we need additional symbols for $d_{i} &gt; 9$. For instance, in hexadecimal: $0, 1, 2, \ldots, 9, \mathrm{a}=10, \mathrm{b}=11, \mathrm{c}=12, \mathrm{d}=13, \mathrm{e}=14, \mathrm{f}=15$.

int('11111100101', base=2) == 0b11111100101 == 2021  # binary

int('7e5', base=16) == 0x7e5 == 2021  # hexadecimal

int('3745', base=8) == 0o3745 == 2021  # octal```

**Base conversion**

Again going from base10 to base 2, need to split into two parts. 

Integer part:
can write instead of polynomial in this manner:

Integer part
We can write an integer $x$ in nested polynomial form:
$$
\begin{split}
x &amp;= (c_{n}c_{n-1} \ldots c_{1}c_{0})_{\beta} \\
  &amp;= \sum_{i=0}^{n} c_{i} \times \beta^{i} \\
  &amp;= c_{0} + \beta(c_{1} + \beta (c_{2} + \beta (\ldots)))
\end{split}
$$
Dividing $x$ by $\beta$ results in remainder $c_{0}$ and quotient $c_{1} + \beta (c_{2} + \beta (\ldots))$.
By repeating the division we obtain digits $c_{0}$, $c_{1}$, $c_{2}$, etc.

**Fractional part**
remainder is c1 for example, and keep iterating back in and dividing by beta.


A real number $x &lt; 1$ in base-$\beta$ can be written as:$$
\begin{split}
x &amp;= \sum_{i=1}^{\infty}c_{i}\beta^{-i} \\
&amp;= (0.c_{1}c_{2}c_{3}\ldots)_{\beta}
\end{split}
$$

If we multiply $x$ by $\beta$, we get:$$
\beta x = (c_{1}.c_{2}c_{3}\ldots)_{\beta}
$$

Digit $c_{1}$ we get by taking the integer part of $\beta x$.

By repeating the multiplication by $\beta$ we obtain all decimal digits (if the number has a finite representation) or until we obtain enough significant digits.

Each time you multiple beta, it moves number one step to the right. 



NB: be careful not to end in infinite loop eg. with fractions or pi. So use the ```ndigits``` functions to limit the loop. 

**octal -> decimal **

In octal decimal system the numbers are from 0-7. Can convert to binary form by replacing ??

**Hexadecimal -> binary**

Group number in groups of four binary digits 

Convert f to binary form eg. f4c5, don't write all the functions.
Hexidecimal is a way to write shortened binary numbers (?). 
0x means it is a decimal number 


Exercise 3: 
Complete the following table

decimal	binary	hexadecimal	octal
2.65			
10011.1101		
f4.c5	

IEEE floating point standard (IEEE-754) 

Let us say we want to write the following constants into memory:

$e = 2.718281828459045...
vacuum permeability: $\mu_{0} = 4\pi \times 10^{-7} {NA}^{-2
Planck's constant: h = 6.626070040 \times 10^{−34} {Js}


Need something more 'clever' than decimal to binary conversion as seen before to represent the shift. This is called scientific notation.

We usually write integer part and fractional part together with a (decimal/radix) point in between.
On the other hand, we can also write:

\begin{split}
37541.23 &amp;= 37.54123 \times 10^{3}\\ 
         &amp;= 3.754123 \times 10^{4}\\
         &amp;= 0.3754123 \times 10^{5}
\end{split}

This representation is not unique. If we allow these representations in memory then it doesn't work ?? 

To ensure uniqueness, we introduce normalised scientific notation:
x = 0.d_{1}d_{2}d_{3}\ldots \times 10^{e}, \quad d_{1} \ne 0

Leading digit in the fractional part is not zero (except when the number is zero):

37541.23 = 0.3754123 \times 10^{5 
0.009765 = 0.9765 \times 10^{-2}

**Normalised scientific notation in decimal form** 

Zero is a special case. Any real number that is not zero can be written as 

**Floating point representation**

We need to save the sign ($\pm$), mantissa ($m$), and exponent ($e$) separatately.
Every computer has a finite word length

We cannot exactly represent:
irrational numbers, e.g. $\pi$, $\mathrm{e}$, ...,
rational numbers that do not fit the finite form, e.g. $\frac{1}{3}$.
A disrete set of numbers that are exactly representable are called machine numbers.
A number with a terminating expansion in one base might have a non-terminating expansion in another base, e.g. (0.1)base10= (0.001100101)2

If one number has a finite form in one base it doesnt mean it will have a finite form in another one. If you don't pass ```ndigits``` then it will just make it an infinite loop. 

###Exercise 4: 

mantissa here has 3 bits: b1 b2 and b3. So all this in total has 3 bits. 1 bit for exponent 2e. Note that we allow b1 b2 and b3 to be 0 or 1


In 'machine numbers' : replacing, doing all the possible combinations using 'itertools.product' 
Note in the solution: there are duplications, because it is not normalised! We allowed numbers to be both 0 and 1. To change that you need to count unique numbers.

If you plot it, you can see it goes from 0 on. 

Overflow: no machine numbers in there (?), have to tell system how to deal with it.
Underflow: usually deal with it by rounding to 0, occurs  when number is under 0. 

Duplicates mean we are wasting space.
Machine numbers are numbers that you can represent in memory. 
Any number larger than machine numbers = overflow. Any number lower than machine numbers = underflow. 

**Standard**

- IEEE-754: established floating-point standard (IEEE-754)
- Before the standard each computer manufacturer developed their own floating-point number systems.
- 3 common levels of precision: 
- single precision: 3 bits in total, need to squeeze flaoting point number in those bits. Need to use 8 bit for the exponent and 23 bits for mantissa.
- DOuble precision (aka two times single): 1 bit for sign, 11 for exponenet and 52 for mantissa

- Single Precision:

see cheat 

**Machine precision and res**

- float of x is not the same as x!
- Machine epsilon: smallest number e I can add to 1 for the number not to be 1.
- The number of real numbers x we can represent is finite.
The floating-point machine number corresponding to $x$, we denote as $\mathrm{fl}(x).

- For single precision, the machine E is:
E = 1. 00000000000000000000000 - 1. 00000000000000000000000 = 2^-23

Precision: just an integer saying how many digits I can rely on, here approx 6 decimal digits because  $\epsilon = \approx 1.19 \times 10^{-7}$

Resolution: Sometimes, instead of precision $p$, we show resolution: $10^{-p} = 10^{-6}$.



Don't have to remember all this, can be access through Numpy .
```single= np.finfo(np.float32)```


**Double Precision**

Same as single precision, but multiplied by 2.  So 64 bit.
- You instead have e -1023
- for mantissa: 52 bits with normalised one-plus form to ensure normalisation.
- largest mantissa = 1.8x10^308

- Machine epsilon: epsilon =2-52 = 2.2 x10^-16
```double =np.finfo(np.float64)```


#Exercise 5: split it in two integers, normalise it, and convert it

#Exercise 6: opposite, using grouping, from binary to decimal. 

NB: everything in f are zeroes or 1. 

- Numbers such as x=2^687362 cannot be represented, it is overflow

**Chopping and rounding**

For simplicity, here, we assume single precision floating-point numbers.
Let us say we want to represent $x$ with its nearest machine number


... -> See sheet

**Loss of significance** 

Let us say we need to subtract two nearly equal numbers in a machine with only 5 decimal digits of accuracy:
x = 0.8796421358
y = 0.8796354261

When doing x-y. this is correct. But are there machine numbers? yes probably making 2 errors. But much smaller when you restrict yourself to 5 decimal places. When rounding to 6 (so 5 digits) you can compute absolute and relative. 

You need to take some steps to avoid that. 

**Theorem of loss of precision**

How many significant binary digits are lost in $x - y$ when $x$ is close to y?

Theorem: Let x and y be normalised floating-point machine numbers, where $x &gt; y &gt; 0. If 2^{-p} \le 1 - \frac{x}{y} \le 2^{-q}$ for some positive integers $p$ and q, then at most p and at least q significant binary bits are lost in the subtraction $x - y$.
This is the measure of how close two numbers are. Compute the middle statement and for some positive integers p and q.  So some bits are lost to that computation.

#Exercise 7: how many binary digits you lost?


**Why is x==y bad?**

x = np.float64(1)
y = np.float64(1/3)

assert x == 3*y

Above this is double precision.


Below this is single precision. This doesn't work. When representing in computer memory, 0.1 is saved as a number close to 0.1 in machine numbers (relative error). 

x = np.float32(1)
y = np.float32(1/3)

assert x == 3*y

assert 0.1 + 0.2 == 0.3



For comparison of floating-point numbers, we use ```np.isclose.```


```assert np.isclose(x, 3*y)```

To define how close it is, use ```rotl= number``` to define relative tolerance such as 1e-5 for 5 decimals. Can also use ```atol=number```

With numpy arrays, use ```np.allclose```


























