from sympy.plotting import plot
import sympy as sp
from sympy import solve, symbols
import collections

import matplotlib.pyplot as plt
import numpy as np
import numpy.linalg as la


def plot_lines(*eqs, solvefor='y'):
    plot(*[solve(e,solvefor)[0] for e in eqs])


def create_vd(v):
    if isinstance(v[0], collections.Sequence):
        if len(v) > 2:
            return (v[0][0], v[0][1], v[1][0], v[1][1])
        else:
            return (0,0,v[0][0],v[0][1])
    else:
        return (0,0,v[0], v[1])
def extract_color(v):

    return v[-1]
    #if isinstance(v[0], collections.Sequence):
    #    return v[1]
    #else:
    #    return v[2]

def draw_vectors(*v, ax=None):


    vs = [create_vd(vv) for vv in v]

    soa =np.array(vs)
    if ax == None:
        plt.figure()
        ax = plt.gca()

    maxx = max([abs(vvv) for vv in vs for vvv in vv])

    colors = [extract_color(vv) for vv in v]
    for vv,c in zip(vs, colors):
        ax.arrow(*vv, color = c, head_width=0.1*maxx, head_length=0.1*maxx)

    ax.set_xlim([-1.2*maxx, 1.2*maxx])
    ax.set_ylim([-1.2*maxx, 1.2*maxx])
    ax.set_aspect("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.draw()
    plt.show()
