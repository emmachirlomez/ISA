# This is a way to implement a multiplication of a list by a constant
# This method uses the recursive definition of multiplication
# This method also uses recursion to run through the list
# The constant is represented by C 
# The element being multiplied is represented by elem

# Loading values for jump instructions
0 : LI R5, 10
1 : LI R6, 2

2: LI R4, 0;         # R4 will be the register saving the result
3: LD R15, R12:      # Loads c to register R15
4: LD R14, R10;      # Loads the elem to be multiplied
5: ADD R4, R4, R14   # recursive mult (A*B = A+A and B-1 until B = 0)

6: JEQ R5, R0, R15   # if R15 is 0 move to next elem
7: SUB R15, R15, R1  # subtracts 1 from c       
8: JR R6             # loops back with c-1
9: SD R4, R10        # saves elem after multiplication

10: ADD R10, R10, R1 # moves pointer R10 to next elem
11: JLT 29, R11, R10 # ends the subroutine after going through the last elem
12: JR R1            # Loops back to step (2) if there is still elements to be multiplied