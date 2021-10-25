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

Convert f to binary form eg. f4c5, don't write all the functions









