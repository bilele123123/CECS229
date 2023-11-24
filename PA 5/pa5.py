from vec import Vec


class Matrix:

  def __init__(self, rowsp):
    self.rowsp = rowsp
    self.colsp = self._construct_colsp(rowsp)

  def set_row(self, i, new_row):
    if len(new_row) != len(self.rowsp[0]):
      raise ValueError("Incompatible row length.")
    self.rowsp[i - 1] = new_row
    self.colsp = self._construct_colsp(self.rowsp)

  def set_col(self, j, new_col):
    if len(new_col) != len(self.colsp[0]):
      raise ValueError("Incompatible column length.")
    for i in range(len(self.rowsp)):
      self.rowsp[i][j - 1] = new_col[i]
    self.colsp = self._construct_colsp(self.rowsp)

  def set_entry(self, i, j, val):
    if not (1 <= i <= len(self.rowsp) or 1 <= j <= len(self.colsp[0])):
      raise IndexError("Incompatible index value, index out of bounds.")
    self.rowsp[i - 1][j - 1] = val
    self.colsp = self._construct_colsp(self.rowsp)

  def get_row(self, i):
    if not (1 <= i <= len(self.rowsp)):
      raise IndexError("Incompatible index value, index out of bounds.")
    return self.rowsp[i - 1]

  def get_col(self, j):
    if not (1 <= j <= len(self.colsp)):
      raise IndexError("Incompatible index value, index out of bounds.")
    column = []
    for row in self.rowsp:
      column.append(row[j - 1])
    return column

  def get_entry(self, i, j):
    if not (1 <= i <= len(self.rowsp) or 1 <= j <= len(self.colsp[0])):
      raise IndexError("Incompatible index value, index out of bounds.")
    return self.rowsp[i - 1][j - 1]

  def col_space(self):
    column_space = []
    for i in range(len(self.colsp)):
      column_space.append(self.colsp[i])
    return column_space

  def row_space(self):
    row_space = []
    for i in range(len(self.rowsp)):
      row_space.append(self.rowsp[i])
    return row_space

  def get_diag(self, k):
    if k == 0:
      min_dim = min(len(self.rowsp), len(self.rowsp[0]))
      diagonal = []
      for i in range(min_dim):
          if i < len(self.rowsp) and i < len(self.rowsp[0]):
              diagonal.append(self.rowsp[i][i])
      return diagonal

    elif k > 0:
      diagonal = []
      for i in range(len(self.rowsp) - k):
        if i + k < len(self.rowsp[0]):
          diagonal.append(self.rowsp[i][i + k])
      return diagonal

    elif k < 0:
      diagonal = []
      for i in range(len(self.rowsp) + k):
        if i - k < len(self.rowsp[0]):       
          diagonal.append(self.rowsp[i - k][i])
      return diagonal


  """
  INSERT MISSING SETTERS AND GETTERS HERE
  """

  def _construct_colsp(self, rowsp):
    colsp = []
    if not rowsp:
      return colsp
    rowsp = [row for row in rowsp if isinstance(row, (list, tuple))]
    if not rowsp:
      return colsp
    min_length = min(len(row) for row in rowsp)
    for j in range(min_length):
      col = [row[j] for row in rowsp]
      colsp.append(col)
    return colsp

  def _construct_rowsp(self, colsp):
    rowsp = []
    if not colsp:
      return rowsp
    colsp = [col for col in colsp if isinstance(col, (list, tuple))]
    if not colsp:
      return rowsp
    min_length = min(len(col) for col in colsp)
    for i in range(min_length):
      row = [col[i] for col in colsp]
      rowsp.append(row)
    return rowsp

  def __add__(self, other):
    if len(self.rowsp) != len(other.rowsp) or len(self.rowsp[0]) != len(other.rowsp[0]):
      raise ValueError("Incompatible matrix dimensions for matrix addition.")
    result = []
    for i in range(len(self.rowsp)):
      result_row = []
      for j in range(len(self.rowsp[0])):
        result_row.append(self.rowsp[i][j] + other.rowsp[i][j])
      result.append(result_row)
    return Matrix(result)

  def __sub__(self, other):
    if len(self.rowsp) != len(other.rowsp) or len(self.rowsp[0]) != len(other.rowsp[0]):
      raise ValueError("Incompatible matrix dimensions for matrix subtraction.")
    result = []
    for i in range(len(self.rowsp)):
      result_row = []
      for j in range(len(self.rowsp[0])):
        result_row.append(self.rowsp[i][j] - other.rowsp[i][j])
      result.append(result_row)
    return Matrix(result)

  def __mul__(self, other):
    if type(other) == float or type(other) == int:
      result = []
      for i in range(len(self.rowsp)):
        result_row = []
        for val in self.rowsp[i]:
          result_row.append(val * other)
        result.append(result_row)
      return Matrix(result)

    elif type(other) == Matrix:
      if len(self.rowsp[0]) != len(other.rowsp):
        raise ValueError("Incompatible matrix dimensions for matrix multiplication.")
      result = []
      for i in range(len(self.rowsp)):
        result_row = []
        for j in range(len(other.rowsp[0])):
          dot_product = 0
          for k in range(len(other.rowsp)):
            dot_product += self.rowsp[i][k] * other.rowsp[k][j]
          result_row.append(dot_product)
        result.append(result_row)
      return Matrix(result)

    elif type(other) == Vec:
      if len(self.rowsp[0]) != len(other.elements):
        raise ValueError("Incompatible dimensions for matrix-vector multiplication.")
      result = []
      for i in range(len(self.rowsp)):
        dot_product = 0
        for j in range(len(other.elements)):
          dot_product += self.rowsp[i][j] * other.elements[j]
        result.append(dot_product)
      return Vec(result)

    else:
      print("ERROR: Unsupported Type.")
    return

  def __rmul__(self, other):
    if type(other) == float or type(other) == int:
      result = []
      for i in range(len(self.rowsp)):
        result_row = []
        for val in self.rowsp[i]:
          result_row.append(other * val)
        result.append(result_row)
      return Matrix(result)
    else:
      print("ERROR: Unsupported Type.")
    return

  '''-------- ALL METHODS BELOW THIS LINE ARE FULLY IMPLEMENTED -------'''

  def __str__(self):
    """prints the rows and columns in matrix form """
    mat_str = ""
    for row in self.rowsp:
      mat_str += str(row) + "\n"
    return mat_str

  def __eq__(self, other):
    """overloads the == operator to return True if 
      two Matrix objects have the same row space and column space"""
    return self.row_space() == other.row_space() and self.col_space(
    ) == other.col_space()

  def __req__(self, other):
    """overloads the == operator to return True if 
      two Matrix objects have the same row space and column space"""
    return self.row_space() == other.row_space() and self.col_space(
    ) == other.col_space()
