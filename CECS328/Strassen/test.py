import numpy as np
#117 137 185 -2388
def pad_matrix(matrix):
    size = matrix.shape[0]
    next_power_of_2 = 2 ** int(np.ceil(np.log2(size)))
    if size < next_power_of_2:
        padding = next_power_of_2 - size
        return np.pad(matrix, ((0, padding), (0, 0)), mode='constant', constant_values=0)
    return matrix

def strassen_multiply(a, b):
    size = len(a)

    if size <= 32:  # Use standard multiplication for small matrices
        return np.dot(a, b)

    # Ensure matrices are of the same size
    if a.shape != b.shape:
        raise ValueError("Matrix dimensions do not match")

    # Pad matrices to the nearest power of 2
    a = pad_matrix(a)
    b = pad_matrix(b)

    size = a.shape[0]  # Update size after padding

    half_size = size // 2

    # Check if the matrix has enough rows for splitting
    if size < 4:
        raise ValueError("Matrix does not have enough rows for splitting")

    a11, a12, a21, a22 = np.array_split(a, 2, axis=0)
    b11, b12, b21, b22 = np.array_split(b, 2, axis=1)

    # ... (rest of your code)

# Rest of your code...


# Perform matrix multiplication using Strassen's algorithm
result_strassen = strassen_multiply(a, b)

# Perform matrix multiplication using standard algorithm
result_standard = standard_multiply(a, b)

# Calculate the sum of entries in the result matrix
sum_result_strassen = np.sum(result_strassen)
sum_result_standard = np.sum(result_standard)

print(sum_result_strassen)
print(sum_result_standard)
