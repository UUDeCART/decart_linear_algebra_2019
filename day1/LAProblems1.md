
# Linear Algebra and Biomedical Data Science

## Homework - Work by hand

### Problem  1.1
Using Gaussian elimination solve the following system of equations.

a)
\begin{eqnarray*}
x_1+5x_2&= 7\\
-2x_1-7x_2&=-5
\end{eqnarray*}

b)
Find the point of intersection of the two lines $x_1+5x_2=7$ and $x_1-2x_2=-2$.

c)
\begin{eqnarray*}
x_2+4x_3&= -5\\
x_1+3x_2+5x_3&=-2\\
3x_1+7x_2+7x_3&=6
\end{eqnarray*}

#### Using Python
Redo a), b), and c).

### Problem  1.2
Determine if the system is consistent and if it has a unique  solution. Each matrix represents an augmented matrix.

a)
\begin{equation*}
\begin{bmatrix}
x & * & * & * \\ 
0 & x & * & *\\ 
0& 0 &x &0
\end{bmatrix}
\end{equation*}

b)
\begin{equation*}
\begin{bmatrix}
0 &x& * & * & * \\ 
0 &0& x & * & *\\ 
0& 0&0 &0 &x
\end{bmatrix}
\end{equation*}


Find the general form of the solution for the following augmented matrix

c)
\begin{equation*}
\begin{bmatrix}
1 &-3& 0 & -1 & 0 &-2 \\ 
0 &1&0& 0 & -4 & 1\\ 
0&0& 0&1 &9 &4\\
0&0&0&0&0&0
\end{bmatrix}
\end{equation*}


### Problem 1.3
Let $\mathbf{x}=\begin{bmatrix}
1 \\ 2 \\ 3\\ 4
\end{bmatrix}$, $\mathbf{y}=\begin{bmatrix}
-2 \\ 1\\ 2\\ 1
\end{bmatrix}$, and $\mathbf{z}=\begin{bmatrix}
-2 \\ 1\\ 2
\end{bmatrix}$ .  

a) Find $\mathbf{x}+2\mathbf{y}$ and $-2\mathbf{x}+\mathbf{z}$.

b) Let $\mathbf{x}=\begin{bmatrix}
1 \\ -2 \\ 0
\end{bmatrix}$, $\mathbf{y}=\begin{bmatrix}
0\\ 1\\ 2
\end{bmatrix}$, and $\mathbf{z}=\begin{bmatrix}
5 \\ -6\\ 8
\end{bmatrix}$. Is $\mathbf{b}= \begin{bmatrix}
2 \\ -1\\ 6
\end{bmatrix}$ a linear combination of $\mathbf{x}$, $\mathbf{y}$, and  $\mathbf{z}$?

c) List 4 vectors which are in the span of $\{\mathbf{v_1},\mathbf{v_2}\}$ where $\mathbf{v_1}=\begin{bmatrix}
2 \\ 2\\ 6
\end{bmatrix}$ and $\{\mathbf{v_2}=\begin{bmatrix}
-2 \\ 2\\ 6
\end{bmatrix}$


#### Using Python 
Let $\mathbf{x}$ be a vector in $\mathbb{R}^{10}$ whose $i$th component is $i$, let $\mathbf{y}$ also be a vector in $\mathbb{R}^{10}$ whose $i$th component is $i^2$, and let $\mathbf{z}$ be a vector in $\mathbb{R}^{11}$ whose components are all 1.

Find $\mathbf{y}+3\mathbf{x}$, $-2\mathbf{z}$, and $\mathbf{x}+\mathbf{z}$.

### Problem 1.4

Compute the product $A\mathbf{x}$ using linear combination of columns and dots products.

a) $A=\begin{bmatrix}
-4& 2\\
1&6\\
0& 1
\end{bmatrix}$ and $\mathbf{x}=\begin{bmatrix}
3\\
-2\\
7
\end{bmatrix}$

b) $A=\begin{bmatrix}
5& 1&-8&4\\
-2 &-7&3&-5
\end{bmatrix}$ and $\mathbf{x}=\begin{bmatrix}
5\\
-1\\
3\\
-2
\end{bmatrix}$

c) a) $A=\begin{bmatrix}
-4& 2\\
1&6\\
0& 1
\end{bmatrix}$ and $\mathbf{x}=\begin{bmatrix}
3\\
-2
\end{bmatrix}$

d) Is $\mathbf{x}=\begin{bmatrix}
0\\
4\\
4
\end{bmatrix}$ in the span of the columns of 
$A=\begin{bmatrix}
3& -5\\
-2&6\\
1& 1
\end{bmatrix}$?

#### Using Python 
Redo a), b) and c) using python.

### Problem 1.5

a) Determine if the system has a non-trivial solution.

\begin{eqnarray*}
2x_1-5x_2+8x_3&= 0\\
-2x_1-7x_2+x_3&=0\\
-4x_1+2x_2+7x_3&=0\\
\end{eqnarray*}

### Problem 1.6
a) Find the values of $h$ which make the following vectors linearly dependent.
$\begin{bmatrix}
1\\
-1\\
4
\end{bmatrix}$, $\begin{bmatrix}
3\\
-5\\
7
\end{bmatrix}$, and 
$\begin{bmatrix}
-1\\
5\\
h
\end{bmatrix}$


```python

```


```python

```
