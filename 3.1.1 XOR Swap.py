# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 19:21:02 2024

@author: Hegel
"""

# 1.Show the test data.
a = 1234
b = 5678

print ("Dec: a={0}, b={1}".format(a, b))
print ("Bin: a={0}, b={1}\n".format(bin(a), bin(b)))

# 2.Swap the two.
a = a ^ b
b = a ^ b
a = a ^ b

# 3.Print the result.
print ("Dec: a={0}, b={1}".format(a, b))
print ("Bin: a={0}, b={1}\n".format(bin(a), bin(b)))

"""
More about the XOR Swap:
See Wikipedia for mathematical proof. 
With associativity and Commutability it's easy to derive the result.
Notice the reduced efficiency due to pipelined CPU designs and data reliance.
Another explanation is through matrix multiplication.
"""
