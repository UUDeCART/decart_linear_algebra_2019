import math
import numpy as np
from numpy.linalg import norm
from collections import defaultdict

class sparsev(defaultdict):
    def __init__(self, *args, dim=1, **kwargs):
        self.__dim = dim
        super(sparsev, self).__init__(*args, **kwargs)
        
    @property
    def dim(self):
        return self.__dim

    def __str__(self):
        rslt =  "(dim=%d) %s"%self.dim
        indices = list(self.keys())
        indices.sort()
        for index in indices:
            rslt = rslt + "| %s |"%("%5.2f"%row).ljust(7)
        return rslt
    def __repr__(self):
        return self.__str__()

def norm(v):
    return math.sqrt(np.sum([vv*vv for vv in v.values()]))
def dot(v1, v2):
    if v1.dim != v2.dim:
        raise ValueError("%d !=%d: the sparse vectors must have the same dimension"%(v1.dim, v2.dim))
    keys = set(v1.keys()).intersection(v2.keys())
    return np.sum([v1[k]*v2[k] for k in keys])


def print_vector(v):
    print(v)
    
def vec_eq(v1, v2):
    """
    checks whether two vectors are equal

    v1:
    v2:
    returns boolean
    """
    assert v1.dim == v2.dim
    
    if v1.keys() != v2.keys():
        return False
    
    for key in v1.keys():
        if v1[key] != v2[key]:
            return False
    return True


def alpha_x_v(alpha, v):
    """
    multiplies vector v by scalar alpha

    returns vector
    """
    newv = sparsev(int, dim=v.dim)
    for index, val in v.items():
        sparsev[index] = alpha*val
    return newv

def v_plus_v(v1, v2):
    """
    vector addition of vectors v1 and v2

    returns vector
    """
    assert v1.dim == v2.dim
    newv = sparsev(int, dim=v.dim)
    keys = set(v1.keys()).union(v2.keys())
    for key in keys:
        newv[key] = v1[key] + v2[key]

    return newv



def zero(n):
    """
    returns a zero vector of dimension n
    """
    return sparsev(int, dim=n)


def cos_sim(v1, v2):
    """
    computes the cosine similarity between two vectors v1 and v2
    Requires a dot product function and a norm function
    """
    return dot(v1,v2) / (norm(v1)*norm(v2))