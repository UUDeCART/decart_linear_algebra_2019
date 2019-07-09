#!/usr/bin/env python
# coding: utf-8

# # Matrices: Column View
# 
# We can also think of matrices as a collection of vectors
# 
# \begin{equation}
# \begin{bmatrix}
# \begin{array}{rr{\qquad}1}
# \pmb{c_1} &
# \pmb{c_2} 
# \end{array}
# \end{bmatrix}
# \pmb{x} =
# \pmb{b}
# \end{equation}
# 
# In this view, we can think of finding the vector $\pmb{x}$ consisting of the scalars $x_1$ and $x_2$ such that the weighted addition of the two vectors (columns of the matrix) on the LHS equals the vector on the RHS:
# 
# \begin{equation}
# x_1\begin{bmatrix}
# \begin{array}{r{\quad}1}
# 2\\ 4
# \end{array}
# \end{bmatrix} 
# + x_2
# \begin{bmatrix}
# \begin{array}{r{\quad}1}
# 4\\ 11
# \end{array}
# \end{bmatrix}=
# \begin{bmatrix}
# \begin{array}{r{\quad}1}
# 2 \\ 1
# \end{array}
# \end{bmatrix}
# \end{equation}

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import sys
sys.path.append("..")
from myla.plotting import *


# In[3]:


sys.path


# ## Column View of Matrices
# 
# We can think of this problem from a different perspective: from the perspective of the columns of \textbf{A}. 
# 
# In this view, we can think of finding the scalars $x_1$ and $x_2$ such that the weighted addition of the two vectors (columns of the matrix) on the LHS equals the vector on the RHS:
# 
# \begin{equation}
# x_1\begin{bmatrix}
# \begin{array}{r{\quad}1}
# 2\\ 4
# \end{array}
# \end{bmatrix} 
# + x_2
# \begin{bmatrix}
# \begin{array}{r{\quad}1}
# 4\\ 11
# \end{array}
# \end{bmatrix}=
# \begin{bmatrix}
# \begin{array}{r{\quad}1}
# 2 \\ 1
# \end{array}
# \end{bmatrix}
# \end{equation}
# 
# From the previous notebook, we know that the solution to the systems of equations is $(x_1=3,x_2=-1)$. We can add vectors graphically by putting the tail of the second vector on the tip of the first vector. The first vector
# 
# \begin{equation}
# 3\begin{bmatrix}
# \begin{array}{r{\quad}1}
# 2\\ 4
# \end{array}
# \end{bmatrix} =
# \begin{bmatrix}
# \begin{array}{r{\quad}1}
# 6\\ 12
# \end{array}
# \end{bmatrix}
# \end{equation}
# 
# is plotted in red and the second vector
# 
# \begin{equation}
# -1\begin{bmatrix}
# \begin{array}{r{\quad}1}
# 4\\ 11
# \end{array}
# \end{bmatrix} =
# \begin{bmatrix}
# \begin{array}{r{\quad}1}
# -4\\ 11
# \end{array}
# \end{bmatrix}
# \end{equation}
# is plotted in green.

# We see that the green vector ends at $(2,1)$ which is the vector on the RHS. This can be verified by explicitly plotting the RHS vector in blue.

# In[5]:


draw_vectors(((0,0),(6,12),'r'),
             ((6,12),(-4,-11),'g'),
             ((0,0),(2,1),'b'))


# ## Problem 
# 
# Representing a Matrix `M` as a list of columns, write a function that multiplies a vector `v` by a matrix `m`.
# 
# Note that the Python representing of `m` will look like rows even though they are columns.
# 
# ```Python
# m = ((2,4),(4,11))
# ```

# In[6]:


from myla.becvector import *


# In[7]:


def print_matrix(m, width=7):
    for row in range(len(m[0])):                     
        print("|",
              " ".join([("%5.2f"%m[col][row]).ljust(width) for col in range(len(m))]),
             "|")


# In[8]:


#print_matrix([(2,4),(4,11)])


# In[70]:


result = []

def m_x_v(m,v):
    #assert len(m[0][0]) == len(v[0])
    #result.append([])
    #for i in range(len(m)):
    #    medio = 0
    #    result.append(i)
    #    for j in range(len(m[i])):
    #        #result[i].append(j)
    #        medio += m[i][j]*v[i]
    #        #print(medio)
    #        result[i]=medio
    #    return result    #return medio
    
    #for col,alpha in zip(m,v);
    #    print(col)
    #    print(alpha)
    
    result = zero(len(m[0]))
    for i in range(len(m)):
        col = m[i]
        col2 = alpha_x_v(v[i], col)
        result = v_plus_v(result, col2)
    return result


# In[71]:


#m_x_v(((2,4),(4,11)), (3,-1))
#print_vector(m_x_v(((2,4),(4,11)), (3,-1)))


# In[79]:


#help(zero)

#a = zero(len(((2,4),(4,11))))
#a

#help(zip)


# In[72]:


def matriz_x_vector(m,v):
    for i in range(len(m)):
        for j in range(len(v)):
            print(m[i][j], v[j])


# In[74]:


#matriz_x_vector(((2,4),(4,11)), (3,-1))


# ## Example: Rotation in the 2D Plane
# 
# A rotation around the origin in the 2D plane by an angle $\phi$ can be described by the matrix
# 
# \begin{equation}
# \pmb{R}_{\phi} = 
# \begin{bmatrix}
# \begin{array}{rr{\qquad}1}
# \cos \phi & -\sin \phi \\
# \sin \phi & \cos \phi 
# \end{array}
# \end{bmatrix}
# \end{equation}
# 
# * Write a program `get_rot` that takes as an argument an angle expressed in either degrees or radians and returns the 
# corresponding rotation matrix. The function should have a keyword argument indicating whether the angle is
# in degrees or radian. 
# 
# * Write a program `rotate_vec` that takes as arguments a 2D vector and an angle and returns the rotated vector.
# 
# * Write a vector `v` and an angle `phi` and returns the angle `v` rotated by the angle `phi`.
# 
# #### Hints 
# * How is `phi` expressed? In Python how are `cos` and `sin` computed?
# 

# In[90]:


#help(math)


# In[118]:


import math
def get_rot(phi, units="degrees"):
    if units=="degrees":
        #phi = math.radians(phi)
        phi = math.pi*phi/180.0
    return [[math.cos(phi), math.sin(phi)],[-math.sin(phi), math.cos(phi)]]
    
    #else:
    #    phi = math.degrees(phi)
    #    [[math.cos(phi), math.sin(phi)],[-math.sin(phi), math.cos(phi)]]
def rotate_vec(v,phi, units="degrees"):
    if units=="degrees":
        r = get_rot(phi, units=units)
    return m_x_v(r,v)


# In[107]:


#print_matrix(get_rot(45))


# In[116]:


#print_matrix(get_rot(math.pi/4, units="radians"))


# In[119]:


#rotate_vec([1,2],45)


# In[121]:


#draw_vectors(((1,0),'r'),
#             (rotate_vec([1,0],-45),'g'))


# ## Matrix-Matrix Multiplication
# 
# We can also think of matrix-matrix multiplication in a column view manner.
# 
# \begin{equation}
# \pmb{A}_{m,n} \pmb{B}_{n,p}=\pmb{C}_{m,p}
# \end{equation}
# 
# $\pmb{A}$ consists of $n$ columns with dimension $m$; $\pmb{B}$ consists of $p$ columns with dimension $n$; the resulting matrix $\pmb{C}$ has $p$ columns of dimension $m$.
# 
# Column $i$ in $\pmb{C}$ is the result of multiplying the $i^{\text{th}}$ vector in $\pmb{B}$ by $\pmb{A}$.
# 
# \begin{equation}
#     \pmb{A}
#     \begin{bmatrix}
#         \begin{array}{rrrr{\qquad}1}
#             \pmb{b}_1 & \pmb{b}_2 & \cdots & \pmb{b}_p
#         \end{array}
#     \end{bmatrix}
# =
#     \begin{bmatrix}
#         \begin{array}{rrrr{\qquad}1}
#             (\pmb{Ab}_1) & (\pmb{Ab}_2) & \cdots & (\pmb{Ab}_p)
#         \end{array}
#     \end{bmatrix}
# \end{equation}
#  
# 

# In[ ]:


from IPython.display import YouTubeVideo


# In[ ]:


YouTubeVideo("FX4C-JpTFgY", start=380, end=608)


# ## Problem:
# #### Looking at a Matrix as a collection of vectors, write a function that computes matrix multiplication column-wise

# In[139]:


def m_x_m(A, B):
    #result = zero(A[0])
    assert len(A) == len(B[0])
    #for i in range(len(B)):
    return [m_x_v(A,b) for b in B]
    #for col_a, col_b in zip(A,B):
    #    print(col_a, col_b)


# In[162]:


def asdsa(A, B):
    result = []
    for b in B:
        result.append(m_x_v(A,b))
    return result


# In[184]:


#import representing_matrices as rp


# In[ ]:


rp.

