# This program gets the n-th fibbonacci number in a complexity of O(log n)
#
# Background maths:
# | a b | . | e f | = | ae+bg af+bh |
# | c d |   | g h |   | ce+dg cf+dh |
#
# By using the notation F(n) = nth Fibbonacci number, we have the recurence:
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2)
# 
# By using our linear algebra skills, we can write this as:
# | 1 1 | . |  F(n)  | = | f(n+1) |
# | 1 0 |   | F(n-1) |   |  f(n)  |
#
# Let A = | 1 1 |
#         | 1 0 |
#

n = 2
|1 1| * |1 1| = | 2 1 | = | 3 2 | = | 5 3 |
|1 0|   |1 0|   | 1 1 |   | 2 1 |   | 3 2 |

# We then want to compute A^n . | 1 |
#                               | 0 |
#
# It's easier said than done, because we need to find a way to compute A^n.
#
# Let's make a subrutine called MatrixExponention which takes the matrix A and a power p and computes A^p.
#
# Pesudocode for the exponentiation of the matrix:
#   def MatrixExponentiation(m : matrix, p : power):
#       ans = I2 (Unit matrix)
#       while p > 0:
#           if p % 2 == 1:
#               ans = ans * m
#           m = m * m
#           p /= 2
#       return ans
#
# We basically need to simulate the code above for a given p, with the matrix A.
# After that, the answer will be the second element of A^n * (1, 0),
# which is R8.
#
# Input: the first position of the RAM will contain n.
# Output: the second position of the RAM will contain F(n). 


# Main
# Reads n from the input, and calls the exponentation subrutine
0: LI R0, 0;            # Set R0 = 0
1: LI R1, 1;            # Set R1 = 1
2: LD R10, R0;          # Load n from RAM(0)
3: LI R3, ...;          # Set adress of MatrixExponantiation
4: JR R3;               # Jump to subrutine
5: NOP;                 # Jump back from MatrixExponantiation
6: SD R8, R1;           # Save answer to position in RAM of R1
7: NOP;
8: NOP;
9: NOP;

# Looking at the pseudocode from the file's description,
# this subrutine makes the "m = m * m" operation
# | R2 R3 | ^ 2 
# | R4 R5 | 
...

# Looking at the pseudocode from the file's description,
# this subrutine makes the "ans = ans*m" operation

...


# MatrixExponentiation subrutine

...
