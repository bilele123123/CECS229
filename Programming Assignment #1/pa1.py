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
    q = n
    while q != 0:
        digit = q % b

        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
            if digit in hex_dict:
                digit = hex_dict[digit]

        digits.append(digit)

        q //= b

    b_expansion_str = ''.join(map(str, reversed(digits)))
    return b_expansion_str
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
    
        # Calculate the sum of the current digits and the carry
        sum_ab_carry = a_i + b_i + carry
        
        # Append the result digit to the left of the current result
        result = str(sum_ab_carry % 2) + result
        
        # Update the carry for the next iteration
        carry = sum_ab_carry // 2

    # If there's a carry left, add it to the result
    if carry == 1:
        result = '1' + result

    return result
""" ---------------- PROBLEM 4 ----------------"""
def binary_mul(a, b):
    # Removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')

    # multiplication algorithm
    partial_products = []
    i = 0 # index of the current binary bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
            # FIXME: See next line
            # Generate the appropriate partial product and append it to the list
            partial_product = b + "0" * i  # Pad 'b' with zeros
            partial_products.append(partial_product)
        i += 1

    # Initialize the result to '0' (binary representation)
    result = '0'

    while len(partial_products) > 0:
        # FIXME: See next line
        # Add the current partial product to the result manually
        current_partial_product = partial_products[0]
        max_len = max(len(result), len(current_partial_product))
        result = result.zfill(max_len)
        current_partial_product = current_partial_product.zfill(max_len)
        carry = 0
        temp_result = ""
        for j in range(max_len - 1, -1, -1):
            bit_result = int(result[j])
            bit_current_partial = int(current_partial_product[j])
            sum_bits = bit_result + bit_current_partial + carry
            temp_result = str(sum_bits % 2) + temp_result
            carry = sum_bits // 2
        if carry:
            temp_result = "1" + temp_result
        result = temp_result
        del partial_products[0]

    # FIXME: See next line
    return result 