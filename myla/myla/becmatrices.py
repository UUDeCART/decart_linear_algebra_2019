from  . becvector import *
import math


def print_matrix(m, width=7):
    for row in range(len(m[0])):                     
        print("|",
              " ".join([("%5.2f"%m[col][row]).ljust(width) for col in range(len(m))]),
             "|")


def m_x_v(m,v):
    assert len(m) == len(v)
    rslt = zero(len(m[0]))
    for col,alpha in zip(m,v):
        col2 = alpha_x_v(alpha, col)
        rslt = v_plus_v(rslt, col2)
    return rslt    


def get_rot(phi, units="degrees"):
    if units.lower()[0] == "d":
        phi = math.pi*phi/180.0
    return [[math.cos(phi),math.sin(phi)],[-math.sin(phi), math.cos(phi)]]

def rotate_vec(v,phi, units="degrees"):
    r = get_rot(phi, units=units)
    return m_x_v(r,v)

def m_x_m(A, B):
    return [m_x_v(A, b) for b in B]
