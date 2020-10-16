# Notations used for making the F(n) thingy

* R0 = 0
* R1 = 1

In MatrixExponentiation:
* R2-R5 = m
* R6-R9 = ans
* R10 = p

# Pesudocode for the exponentiation of the matrix:
#   def MatrixExponentiation(m : matrix, p : power):
#       ans = I2 (Unit matrix)
#       bit = 1
#       while bit <= p:
#           if (p & bit) == bit:
#               ans = ans * m
#           m = m * m
#           bit *= 2
#       return ans
#   0100111 = 01 00001 000001 0000001