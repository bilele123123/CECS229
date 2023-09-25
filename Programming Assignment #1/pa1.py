import math

""" ---------------- PROBLEM 1 ----------------"""
def equiv_to(a, m, low, high):
    # FIXME: Initialize k_low =
    k_low = math.floor((low - a) / m)
    # FIXME: Initialize k_high =
    if high >= a:
        k_high = math.floor((high - a) / m)
    else:
        k_high = math.floor((high - a - 1) / m)
    # FIXME: initialize x_vals
    x_vals = []
    for k in range(k_low - 1, k_high + 1):
        x = k * m + a;
        if low <= x <= high:
            x_vals.append(x)
    return x_vals

""" ---------------- PROBLEM 2 ----------------"""
def b_expansion(n, b):
    digits = []  # stores the digits of the b-expansion
    check = n
    while check != 0:
        digit = check % b

        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            if digit in hex_dict:
                digit = hex_dict[digit]

        digits.append(digit)
        check //= b

    b_expansion = ''.join(map(str, reversed(digits)))
    return b_expansion
""" ---------------- PROBLEM 3 ----------------"""
def binary_add(a, b):
    # Removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # Padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" * diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" * diff + b
    
    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])
    
        sum_carry = a_i + b_i + carry
        result = str(sum_carry % 2) + result
        carry = sum_carry // 2
    if carry == 1:
        result = '1' + result

    return result
""" ---------------- PROBLEM 4 ----------------"""
def binary_mul(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # multiplication algorithm
    partial_products = []
    i = 0  # tracks the index of the current binary bit of string 'a' beginning at 0
    for bit in reversed(a):
        if bit == '1':
            partial_product = b + '0' * i  # Append zeros to the end
            partial_products.append(partial_product)
        i += 1

    result = '0'
    while len(partial_products) > 0:
        result = binary_add(result, partial_products[0])
        del partial_products[0]

    return result
