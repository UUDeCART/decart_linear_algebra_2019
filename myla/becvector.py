import math
def vec_eq(v1, v2):
    """
    checks whether two vectors are equal

    v1:
    v2:
    returns boolean
    """
    assert len(v1) == len(v2)
    for i in range(len(v1)):
        if v1[i] != v2[i]:
            return False
    return True


def alpha_x_v(alpha, v):
    """
    multiplies vector v by scalar alpha

    returns vector
    """
    return [alpha*r for r in v]

def v_plus_v(v1, v2):
    """
    vector addition of vectors v1 and v2

    returns vector
    """
    assert len(v1) == len(v2)
    return [v1[i]+v2[i] for i in range(len(v1))]


def dot(v1,v2):
    """
    computes the dot product between two vectors

    returns scalar
    """

    assert len(v1) == len(v2)
    rslt = 0.0
    for i in range(len(v1)):
        rslt = rslt + v1[i]*v2[i]
    return rslt

def zero(n):
    """
    returns a zero vector of dimension n
    """
    return [0.0 for i in range(n)]

def print_vector(v):
    for row in v:                     
        print("|",
              ("%5.2f"%row).ljust(7),
             "|")
        
def norm(v):
    rslt = 0.0
    for row in v:
        rslt += row*row
    return math.sqrt(rslt)
def cos_sim(v1, v2):
    """
    computes the cosine similarity between two vectors v1 and v2
    Requires a dot product function and a norm function
    """
    return dot(v1,v2) / (norm(v1)*norm(v2))