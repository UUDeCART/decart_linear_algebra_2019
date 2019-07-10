import math
import numpy as np
from numpy.linalg import norm

def vec_eq(v1, v2):
    """
    checks whether two vectors are equal

    v1:
    v2:
    returns boolean
    """
    return np.allclose(v1,v2)


def alpha_x_v(alpha, v):
    """
    multiplies vector v by scalar alpha

    returns vector
    """
    return alpha*v

def v_plus_v(v1, v2):
    """
    vector addition of vectors v1 and v2

    returns vector
    """
    return v1+v2


def dot(v1,v2):
    """
    computes the dot product between two vectors

    returns scalar
    """
    return np.inner(v1,v2)


def zero(n):
    """
    returns a zero vector of dimension n
    """
    return np.zeros(n)

def print_vector(v):
    for row in v:                     
        print("|",
              ("%5.2f"%row).ljust(7),
             "|")
        
#def norm(v):
#    return 
def cos_sim(v1, v2):
    """
    computes the cosine similarity between two vectors v1 and v2
    Requires a dot product function and a norm function
    """
    return dot(v1,v2) / (norm(v1)*norm(v2))