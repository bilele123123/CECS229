import math

""" ---------------- PROBLEM 1 ----------------"""
def equiv_to(a, m, low, high):
    # FIXME: Initialize k_low =
    k_low = math.floor((low + a - 1) / m)
    # FIXME: Initialize k_high =
    k_high = math.floor(high / m)
    # FIXME: initialize x_vals
    x_vals = []
    for k in range(k_low, k_high + 1):
        x = k * m + a;
        if low <= x <= high:
            x_vals.append(x)
    return x_vals

""" ---------------- PROBLEM 2 ----------------"""
def b_expansion(n, b):
    digits = [] # stores the digits of the b-expansion
    q = n
    while q != 0:
        # FIXME: Initialize digit = ...
        if b == 16 and digit > 9:
            hex_dict = {10: 'A', 11 : 'B', 12: 'C', 13: 'D', 14: 'E', 15 : 'F'}
            # FIXME: Update digit = ...
        digits.append(digit)
        # FIXME: Update q = ...
    return # FIXME: Return the string of digits
        

""" ---------------- PROBLEM 3 ----------------"""
def binary_add(a, b): 
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # padding the strings with 0's so they are the same length
    if len(a) < len(b):
        diff = len(b) - len(a)
        a = "0" *diff + a
    elif len(a) > len(b):
        diff = len(a) - len(b)
        b = "0" *diff + b
    
    # addition algorithm
    result = ""
    carry = 0
    for i in reversed(range(len(a))):
        a_i = int(a[i])
        b_i = int(b[i])
    
        # FIXME: Update result += ....
        # FIXME: Update carry = 
    if carry == 1:
        pass # remove
        # FIXME: Update result += 
    return # FIXME return the appropriate string

""" ---------------- PROBLEM 4 ----------------"""
def binary_mul(a, b):
    # removing all whitespace from the strings
    a = a.replace(' ', '')
    b = b.replace(' ', '')
    
    # multiplication algorithm
    partial_products = []
    i = 0 # index of the current binary bit of string 'a' beginning at 0, right-to-left
    for bit in reversed(a):
        if bit == '1':
          # FIXME: See next line
          partial_products.append("""FIXME: Append the appropriate partial product""")
        i += 1

    result = '0'
    while len(partial_products) > 0:
        # FIXME: See next line
        result = binary_add("FIXME: Input the correct arguments")
        del partial_products[0]
    return # FIXME: Return the appropriate result 