def alpha_x_row(alpha, row):
    return [alpha*r for r in row]

def r1_plus_r2(r1, r2):
    assert len(r1) == len(r2)
    return [r1[i]+r2[i] for i in range(len(r1))]


def all_zeros(m, c):
    for row in m:
        if row[c] != 0:
            return False
    return True


def find_arg_maxabs(col):
    arg_max = 0
    max_val = abs(col[0])
    for i in range(1, len(col)):
        aci = abs(col[i])
        if aci > max_val:
            arg_max = i
            max_val = aci       
    return arg_max

def find_pivot(m, c):
    col = [m[r][c] for r in range(c, len(m))]
    pivot_index = find_arg_maxabs(col)
    return c + pivot_index
    

def swap_rows(m, r1, r2):
    m2 = [row[:] for row in m]
    m2[r1] = m[r2]
    m2[r2] = m[r1]
    return m2

def zero_column(m, c):
    m2 = [row[:] for row in m]
    pivot_val = m[c][c]
    for i in range(c+1, len(m)):
        multiplier = -m2[i][c] / pivot_val
        m2[i] = r1_plus_r2(m2[i], alpha_x_row(multiplier, m2[c]))
    return m2


def normalize_pivot(m, c):
    m2 = [row[:] for row in m]
    multiplier = 1.0/m[c][c]
    m2[c] = alpha_x_row(multiplier, m2[c])
    return m2

def print_matrix(m):
    for row in m:
        print("|",
              "".join([("%5.2f"%v).ljust(7) for v in row]),
             "|")

def forward_elimination(m, verbose=False, tol=1e-8):
    m2 = [row[:] for row in m]
    for i in range(0, len(m2)):
        if verbose:
            print("\niteration %2d\n"%i)
        pivot_pos = find_pivot(m2, i)

        m2 = swap_rows(m2, pivot_pos, i)
        if verbose:
            print_matrix(m2)
            print('after swap_rows '*2)
        m2 = zero_column(m2, i)
        if verbose:
            print_matrix(m2)
            print('after zero_column '*2)
        if abs(m2[i][i]) > tol:
            m2 = normalize_pivot(m2,i)
            if verbose:
                print_matrix(m2)
                print('after normalize_pivot '*2)
    return m2






