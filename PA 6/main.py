import pa6
import numpy as np
from random import randint
from structures import Matrix, Vec
from helpers import initialize_matrices, create_vectors




print("Welcome to the PA #6 Tester")

while True:

  user_in = input(
      "\n" + "-" * 50 +
      "\nWhat would you like to test?\n1.  norm(Vec, p) \n2.  _ref(Matrix)\n3.  rank(Matrix)\n4.  gauss_solve(Matrix, Vec)\n5.  gram_schmidt(S)\nQ.  Quit\n\nEnter your selection: "
  )
  if user_in == '1':
    n = randint(3, 5)
    v = [randint(-10, 10) for i in range(n)]
    for p in [1, 2, 3, 10]:
      print('-'*20)
      print(f"\nTesting norm({v}, {p})...")
      returned = pa6.norm(Vec(v), p)
      expected = np.linalg.norm(np.array(v), ord=p)
      print("\tReturned:", returned)
      print("\tExpected:", expected)
      if returned == expected:
        print("\tTest passed!")
      else:
        print(f"\tTest failed!")
  elif user_in == '2':

    matrix1 = Matrix([[2, -1, -10], [2, 0, -4], [-7, 3, 2]])
    matrix2 = Matrix([[-10, 7, 7, -3, 2], [6, -9, 7, -5, 0], [-2, 7, -3, -6, 2]])
    matrix3 = Matrix([[-7, -9, 4, -9], [2, -9, -3, 3]])
    matrices = [matrix1, matrix2, matrix3]

    expected1 = Matrix([[1.0, -0.5, -5.0], [0.0, 1.0, 6.0], [-0.0, -0.0, 1.0]])
    expected2 = Matrix( [[1.0, -0.7, -0.7, 0.3, -0.2], [-0.0, 1.0, -2.333333333333333, 1.4166666666666665, -0.25], [0.0, 0.0, 1.0, -1.5384615384615388, 0.34615384615384626]])
    expected3 =  Matrix([[1.0, 1.2857142857142858, -0.5714285714285714, 1.2857142857142858], [-0.0, 1.0, 0.16049382716049385, -0.03703703703703702]])
    refs = [expected1, expected2, expected3]
    for matrix, expected in zip(matrices, refs):
      print('-'*20)
      m = len(matrix.rowsp)
      if m > 0:
        n = len(matrix.rowsp[0])
      else:
        n = 0
      print(f"\nTesting _ref(A) for  {m}x{n} matrix A:")
      print(matrix)
      returned = pa6._ref(matrix)
      print("\nReturned:\n", returned)
      print("\nExpected:\n" , expected)



  elif user_in == '3':

    k = randint(3, 5)
    dimensions = [(k, k), (randint(3, 4), randint(5, 6)), (randint(5, 6), randint(3, 4))]
    for (m, n) in dimensions:
      np_matrix, matrix = initialize_matrices(m, n)
      print('-'*20)
      print(f"\nTesting rank(A) for {m}x{n} matrix A:")
      print(matrix)
      returned = pa6.rank(matrix)
      expected = np.linalg.matrix_rank(np_matrix)
      print("Returned:", returned)
      print("Expected:", expected)
      if returned == expected:
        print("Test Passed!")
      else:
        print("Test Failed!")

  elif user_in == '4':
    # Test Case 1
    A1 = [
        [-11, 14, -8, 13, 15, -11, 18, 18, 12, -16, 18, -12, -9],
        [-5, -8, -1, -9, -20, 17, 11, 3, -2, -11, -16, 19, -15],
        [-9, 18, -3, 11, -1, 18, 12, -7, -9, 16, 9, 11, -19],
        [-15, -11, -3, -16, -5, 2, -5, -5, -1, -15, 10, -6, -1],
        [2, -9, -9, 9, 14, 10, 0, -13, 19, -17, 18, 8, 10],
        [-16, 20, -2, 13, 3, 8, -2, -20, -15, -19, -1, -3, 13],
        [-11, -6, 9, -8, 11, -11, -16, -19, 15, -14, 20, 1, -4],
        [7, -16, -5, 0, 1, 2, 6, -16, 12, -8, 3, 15, 1]
    ]
    b1 = [-291, 147, 111, -17, 327, 689, 32, 91]
    
    # Test Case 2
    A2 = [
        [-11, 19, -4, -6, 15],
        [-5, -6, 5, -4, -11],
        [-9, -11, -10, 3, -5],
        [4, -8, 6, 0, 0],
        [-14, 17, 18, -1, -18],
        [-1, 7, 16, 20, -12],
        [-14, 18, -16, 4, -1]
    ]
    b2 = [127, -116, 59, -66, -160, -36, 195]

    # Test Case 1
    print('-'*20)
    print("\nTesting gauss_solve(A, b) for Test Case 1")
    matrix1 = Matrix(A1)
    print("A:\n", matrix1)
    print("\nb:", b1)
    returned1 = pa6.gauss_solve(matrix1, Vec(b1))
    print("\nReturned:\n", returned1)
    print("\nExpected:\n", "Infinitely-many solutions with 5 free variables.")

    # Test Case 2
    print('-'*20)
    print("\nTesting gauss_solve(A, b) for Test Case 2")
    matrix2 = Matrix(A2)
    print("A:\n", matrix2)
    print("\nb:", b2)
    returned2 = pa6.gauss_solve(matrix2, Vec(b2))
    print("\nReturned:\n", returned2)
    print("\nExpected:\n", "[-2.0000000000000018, 1.9999999999999982, -7.000000000000001, 6.0, 5.0]")

    # Test Case 3
    A3 = [
        [2, -14, -20, 13, 15, -1, 3],
        [-8, -7, 13, 7, 19, 14, 16],
        [19, 3, -9, -9, -8, -12, -19],
        [-20, 9, -9, -1, -3, -3, 8],
        [3, -19, 7, 0, -20, -12, -13],
        [-17, 2, -19, -19, -4, 0, -14],
        [-9, -14, -19, 18, 2, -8, 7]
    ]
    b3 = [308, 381, -456, 269, -472, 69, 296]

    # Test Case 4
    A4 = [
        [-338.198, 386.512, -338.198, 217.413, 144.942],
        [8, 20, -14, 16, 16],
        [16, 18, -8, -11, -1],
        [18, -4, -11, -13, 1],
        [-14, 16, -14, 9, 6],
        [-18, 11, -1, 8, 17]
    ]
    b4 = [-5145.44, 62, -132, -339, 213, 239]

    # Test Case 3
    print('-' * 20)
    print("\nTesting gauss_solve(A, b) for Test Case 3")
    matrix3 = Matrix(A3)
    print("A:\n", matrix3)
    print("\nb:", b3)
    returned3 = pa6.gauss_solve(matrix3, Vec(b3))
    print("\nReturned:\n", returned3)
    print("\nExpected:\n", "[-9.0, 2.0, -8.0, 6.0, 7.0, 10.0, 7.0]")

    # Test Case 4
    print('-' * 20)
    print("\nTesting gauss_solve(A, b) for Test Case 4")
    matrix4 = Matrix(A4)
    print("A:\n", matrix4)
    print("\nb:", b4)
    returned4 = pa6.gauss_solve(matrix4, Vec(b4))
    print("\nReturned:\n", returned4)
    print("\nExpected:\n", "None")

  elif user_in == '5':

    S = create_vectors(randint(3, 5))
    A = np.array([v.elements for v in S]).T
    print('-'*20)
    print(f"\nTesting gram_schmidt(S) for S:")
    for v in S:
      print(str(v))
    Q, R = np.linalg.qr(A)
    returned = list(pa6.gram_schmidt(S))

    print("\nReturned:\n")
    for v in returned:
      print(v)

    expected = Q.T
    print("\nExpected:\n")
    for col in expected:
      print(col)

    if len(returned) != len(expected):
      print("Test Failed!")
    else:
      print("\nNOTE:\n(1)  Vectors may appear in different order to expected answer.\n(2)  Negatives may appear at element indices opposite to where they appear in the expected answer. This is still correct.")

  elif user_in.upper() == 'Q':
    break
  else:
    print("Invalid selection.  Please try again.\n")
