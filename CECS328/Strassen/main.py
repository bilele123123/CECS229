import numpy as np
import ast
import os

def replace_content(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Replace {{ with [ and }} with ]
    content = content.replace('{', '[').replace('}', ']')

    with open(file_path, 'w') as file:
        file.write(content)

# Replace content in 9a.txt
replace_content(r'H:\Document\CSULB Spring 23\CECS229\CECS229\CECS328\Strassen\9a.txt')

# Replace content in 9b.txt
replace_content(r'H:\Document\CSULB Spring 23\CECS229\CECS229\CECS328\Strassen\9b.txt')

def standard_multiply(a, b):
    return np.dot(a, b)

def pad_matrix(matrix):
    n = matrix.shape[0]
    
    if n == 0:
        return matrix
    
    next_power_of_2 = 2 ** int(np.ceil(np.log2(n)))
    if n != next_power_of_2:
        padding = next_power_of_2 - n
        matrix = np.pad(matrix, ((0, padding), (0, padding)), mode='constant')
    return matrix

def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        matrix_data = ast.literal_eval(content)
        return np.array(matrix_data)

# Load matrices from files
a = read_matrix_from_file(r"H:\Document\CSULB Spring 23\CECS229\CECS229\CECS328\Strassen\9a.txt")
b = read_matrix_from_file(r"H:\Document\CSULB Spring 23\CECS229\CECS229\CECS328\Strassen\9b.txt")

# Perform matrix multiplication using standard algorithm
result_standard = standard_multiply(a, b)

# Calculate the sum of entries in the result matrix
sum_result_standard = np.sum(result_standard)

print(f"Sum of entries using standard algorithm: {sum_result_standard}")
