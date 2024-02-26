# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 20:18:18 2024

@author: Hegel
"""

# 1. Zero the rightmost 1
x = 25
print("x:dec: {}".format(x))
print("x:bin: {}".format(bin(x)))
print("x-1:bin: {}".format(bin(x-1)))
print("x&(x-1):dec: {}".format(x&(x-1)))
print("x&(x-1):bin: {}".format(bin(x&(x-1))))

# Additional info: the above algo is used to test if a number is the exponential of two.

# 2. Locate the rightmost 1
# print("~(x-1):bin: {}".format(bin(~(x-1))))
# print("x&~(x-1):dec: {}".format(x&~(x-1)))
# print("x&~(x-1):bin: {}".format(bin(x&~(x-1))))

# 3. Swap bits
# Function definition
def swapBits (n, p1, p2):
    #print("function called")
    print ("Task: swap bits (LSB at 0)")
    print ("Exchange the bits at location {0} and {1} of integer {2}".format(p1, p2, n))
    print ("Original binary form: {}".format(bin(n)))
    # Extract the two bits required using &1
    bit_1 = (n >> p1) & 1
    bit_2 = (n >> p2) & 1
    print ("Extract to get :")
    print ("bit_1: {}".format(bin(bit_1)))
    print ("bit_2: {}".format(bin(bit_2)))
    # Use ^ to exchange bits.
    # Leftshift the a^b by p1 units.
    # Bitwise xor with n s.t. only the bit at p1 is replaced.
    temp = bit_1 ^ bit_2
    n = n ^ (temp << p1)
    print ("Keep left p2 and replace right p1 to get")
    print ("Binary: {0}, decimal: {1}".format(n, bin(n)))
    n = n ^ (temp << p2)
    print ("Keep the modified p1 and replace the left p2 to get")
    print ("Binary: {0}, decimal: {1}".format(n, bin(n)))
    print ("which is our final result.")

# Driver code
res = swapBits (28, 0, 3)
print("Result = ", res)

# Below are the most important two bit manipulations.
"""
& i.e. bitwise and
for any bit A, A & 1 gives A itself, A & 0 gives 0.
However, if A contains more than 1 bit, 
A & 0001 is giving the LSB.
"""

"""
 ^ i.e. bitsise xor, different = 1, same = 0.
for any pairs of single bits A and B,
A^0 gives A itself. A^A gives 0.
"""




