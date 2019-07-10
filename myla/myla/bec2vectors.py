#!/usr/bin/env python
# coding: utf-8

# In[72]:


get_ipython().run_line_magic('matplotlib', 'inline')


# # Vectors (Column Vectors)
# 
# A vector is a column of numbers. Vectors are related to a **point** but have an essential geometric meaning.
# 
# Think of the vector $v$ as an arrow pointing from the origin to the
# point $p$. Thus vectors have both magnitude and direction. Obviously the
# order of the elements of $v$ matter.
# 
# Below is a figure illustrating a vector pointing from from the origin ($O$) to a point $A$ at $x=2$ and $y=3$.
# 
# ![An example vector](https://goo.gl/qCxJp3)
# 
# The vector above would be written as
# 
# $\vec{v} = \begin{bmatrix}2\\3\end{bmatrix}$

# ## Elements of a Vector
# The **elements** of the vector are known as **scalars.**
# 
# For our example above, the elements of the vector are $2$ and $3$.
# 
# ## Dimension of a Vector
# The **dimension** of a vector is the number of elements in
# the vector.
# 
# If the elements of the vector come from the real numbers ($\mathbb{R}$), we
# would indicate the **n-space** of the vector as
# $\mathbb{R}^n$.
# 
# For our example above, the dimension of the vector is 2.
# 
# **Note:** We can only visualize two or three dimensional vectors. However, most of the vectors we will look at will have a much higher dimension so we will limit our visualizations to 2D. We can plot the projection of a higher-dimension vector on a 2D or 3D space.

# ## Some Example Vectors
# 
# #### Example
# $v_1 = \begin{bmatrix} 2\\-5\end{bmatrix}$,
# * Elements are $2$ and $-5$
# * Dimension is 2
# 
# #### Example
# $v_2=\begin{bmatrix}7\\9\end{bmatrix}$,
# * Elements are $7$ and $9$
# * Dimension is 2
# 
# #### Example
# $v_3=\begin{bmatrix}-3\\4\\5\end{bmatrix}$.
# * Elements are -3, 4, and 5
# * Dimension is 3
# 
# #### Example
# $v_4=\begin{bmatrix}3\\-7\\-2\end{bmatrix}$.
# * Elements are 3, -7, and -2
# * Dimension is 3
# 
# ### Row vectors
# 
# We can also have [**row vectors**](https://en.wikipedia.org/wiki/Row_and_column_vectors). A row vector is the [**transpose**](https://en.wikipedia.org/wiki/Transpose) of a (column) vector. Similarly, a column vector is the transpose of a row vector.
# 
# **transpose** of a column vector. $$v_3^T=\begin{bmatrix}3&4&5\end{bmatrix}$$

# ## Vector Equality
# Vectors are equal when every corresponding elements of the vectors are
# equal. That is, the $i^{th}$ element in vector $a$ corresponds to the $i^{th}$ element in vector $b$ for all $i$.
# 
# ## Representing a Vector in Python
# 
# Python does not have a native vector type, so what are the native Python data structures that we might use to represent an array? 
# 
# * List?
# * Tuple?
# * Dictionary?
# * Set?
# 

# In[1]:


def vec_eq(v1, v2):
    """
    checks whether two vectors are equal
    
    v1: 
    v2:
    """
    assert len(v1) == len(v2)
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            return False
    return True


# In[3]:


vec_eq([1,2],[1,3])


# In[4]:


def alpha_x_v(alpha, v):
    """
    multiplies vector v by scalar alpha
    """
    return [v[i]*alpha for i in range(len(v))]


# In[5]:


alpha_x_v(3,[1,2,3])


# In[9]:


def v_plus_v(v1, v2):
    """
    vector addition of vectors v1 and v2
    """
    return [v1[i]+v2[i] for i in range(len(v1))]


# In[10]:


v_plus_v([1,2,3],[3,6,9])


# In[1]:


def dot(v1, v2):
    """
    Computes the dot product between two vectors
    
    returns scalar
    """
    result = 0
    for i in range(len(v1)):
        result += v1[i]*v2[i]
    return result
    
    


# In[3]:


#dot([1,2],[1,2])


# #### Exercise: Using only `alpha_x_v` and `v_plus_v`, how would you solve the following problem?
# 
# \begin{equation}
# 5 \begin{bmatrix}3\\-7\\-2\end{bmatrix} - \begin{bmatrix}2\\12\\5\end{bmatrix}
# \end{equation}

# In[15]:


#v_plus_v(alpha_x_v(5,[3,-7,-2]),alpha_x_v(-1,[2,12,5]))


# In[16]:


#v_plus_v([1,2,3,4],alpha_x_v(2,[-2,1,2,1]))


# In[42]:


#def m_x_v(m, v):
##    """
    #vector has to be the same size (have the same number of columns as m)
    #return is an m size vector
    
    #"""
    
    #for i in range(len(m)):
    #    for j in range(len(m[i])):
    #        print(m[i][j]*v[i])
   # 


# In[40]:


#m_x_v(matrix,[1,2,3,4])


# In[28]:


#matrix = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
#len(matrix)
#type(matrix)


# In[25]:


#matrix[:]
#len(matrix[0])


# In[15]:


#w, h = 2, 3;
#Matrix = [[0 for x in range(w)] for y in range(h)]


# In[16]:


#Matrix


# In[41]:


#len(matrix[0])
#for i in range(3):
#    print(i)


# In[5]:


#m_x_v(matrix,[1,2])

