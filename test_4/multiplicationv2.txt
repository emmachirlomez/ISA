# This the recursive implementation of the multiplication of 2 integers
# a*b = c
# a will be represented by R14
# b will be represented by R15
# we assume that this values are already loaded to the registers
# we will keep using the notation defined on test 3
# The python representation of this:
# def mult (a,b):
#   if b == 0:
#       return a
#   else:  a = a + mult(a, b-1)
#   



0: LI R3, 8          # Load pointer for jump instruction
1: LI R4, 0          # R4 will be the register used to save the result
2: LI R5, 4          # Load pointer for jump instruction
3: LI R6, 29         # Load pointer for jump instruction
4: ADD R4, R4, R14    
5: SUB R15, R15, R1
6: JLT R3, R15, R1
7: JR R5
8: JR R6