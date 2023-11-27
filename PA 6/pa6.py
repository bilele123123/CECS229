import copy
from structures import Matrix, Vec

""" ----------------- PROBLEM 1 ----------------- """


def norm(v: Vec, p: int):
    """
    returns the p-norm of Vec v
    INPUT:
        p - an integer determining the norm to be calculated
        v - the Vec object for which the norm will be applied
    OUTPUT:
        the norm as a float
    """
    if p == 2:
        return abs(v)
    elif p == 1:
        return sum(abs(x) for x in v)
    else:
        return sum(abs(x) ** p for x in v) ** (1 / p)


""" ----------------- PROBLEM 2 ----------------- """


def _ref(A: Matrix):
    """
    Returns the Row Echelon Form of the Matrix A.

    INPUT: Matrix A
    OUTPUT: distinct Matrix object that is the Row-Echelon Form of A
    """
    matrix = Matrix(copy.deepcopy(A.rowsp))
    m = len(matrix.rowsp)
    if m > 0:
        n = len(matrix.rowsp[0])
    else:
        n = 0
    pivot_row = 0

    for j in range(n):
        nonzero_row = pivot_row
        while nonzero_row < m and matrix.rowsp[nonzero_row][j] == 0:
            nonzero_row += 1

        if nonzero_row == m:
            continue

        matrix.rowsp[pivot_row], matrix.rowsp[nonzero_row] = (
            matrix.rowsp[nonzero_row],
            matrix.rowsp[pivot_row],
        )

        pivot_element = matrix.rowsp[pivot_row][j]
        matrix.rowsp[pivot_row] = [
            elem / pivot_element for elem in matrix.rowsp[pivot_row]
        ]

        for i in range(pivot_row + 1, m):
            factor = matrix.rowsp[i][j]
            matrix.rowsp[i] = [
                elem - factor * matrix.rowsp[pivot_row][index]
                for index, elem in enumerate(matrix.rowsp[i])
            ]

        pivot_row += 1

        if pivot_row == m:
            break

    return matrix


""" ----------------- PROBLEM 3 ----------------- """


def rank(A: Matrix):
    """
    returns the rank of the given Matrix object
    as an integer
    """
    ref_A = _ref(A)
    rank = sum(1 for row in ref_A.rowsp if find_leading_entry(row) != -1)
    return rank

def find_leading_entry(row):
    """
    Finds the index of the first non-zero entry in a row.
    Returns -1 if all entries are zero.
    """
    for i, entry in enumerate(row):
        if entry != 0:
            return i
    return -1

""" ----------------- PROBLEM 4 ----------------- """


def gauss_solve(A: Matrix, b: Vec):
    """
    returns the solution to the system Ax = b 
    if the system has a solution.  If the system
    does not have a solution, None is returned.
    If the system has infinitely-many solutions,
    the number of free variables as an 'int' is returned
    
    INPUT:
        A - a Matrix object
        b - a Vec object

    OUTPUT:
        Vec object if the system has a unique solution
        None if the system has no solution
        int if the system has infinitely-many solutions
    """
    matrix = Matrix(copy.deepcopy(A.rowsp))
    m = len(matrix.rowsp)
    if m > 0:
        n = len(matrix.rowsp[0])
    else:
        n = 0

    for i in range(m):
        matrix.rowsp[i].append(b[i])

    pivot_row = 0
    free_variables = 0

    for j in range(min(m, n)):
        nonzero_row = next((i for i in range(pivot_row, m) if matrix.rowsp[i][j] != 0), -1)

        if nonzero_row == -1:
            free_variables += 1
            continue

        matrix.rowsp[pivot_row], matrix.rowsp[nonzero_row] = matrix.rowsp[nonzero_row], matrix.rowsp[pivot_row]

        pivot_element = matrix.rowsp[pivot_row][j]
        matrix.rowsp[pivot_row] = [elem / pivot_element for elem in matrix.rowsp[pivot_row]]

        for i in range(m):
            if i != pivot_row:
                factor = matrix.rowsp[i][j]
                matrix.rowsp[i] = [elem - factor * matrix.rowsp[pivot_row][index] for index, elem in enumerate(matrix.rowsp[i])]

        pivot_row += 1

        if pivot_row == m:
            break

    for i in range(pivot_row, m):
        if matrix.rowsp[i][-1] != 0:
            return None 

    for i in range(m):
        if all(matrix.rowsp[i][j] == 0 for j in range(n)) and matrix.rowsp[i][-1] != 0:
            return None 

    solution = Vec([matrix.rowsp[i][-1] for i in range(min(m, n))])

    if pivot_row < n:
        free_variables += n - pivot_row
        return free_variables
    else:
        return solution 

""" ----------------- PROBLEM 5 ----------------- """


def gram_schmidt(S: set):
    """
    returns the orthonormal basis of given set S
    INPUT: S - a set of linearly independent 'Vec' objects
    OUTPUT: An orthonormal set of 'Vec' objects
    """
    vectors = list(S)

    ortho_basis = []
    for i in range(len(vectors)):
        vi = vectors[i]
        for j in range(i):
            vi -= (vi * ortho_basis[j]) / (ortho_basis[j] * ortho_basis[j]) * ortho_basis[j]
        ortho_basis.append(vi / abs(vi))

    return set(ortho_basis)