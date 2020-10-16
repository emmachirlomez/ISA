# Implementation of the multiplication

## Main
## Reads a and b from the input, and calls the QuickMultiply subroutine. 
0: NOP;                 # Begin of program
1: LI R1, 1;            # Set R1 = 1
2: LD R2, R0;           # Load 1 from RAM(0)
3: LD R3, R1;           # Load b from RAM(1)
4: LI R6, 16;           # Set adress of QuickMultiply
5: JR R6;               # Jump to subrutine
6: NOP;                 # Jump back from QuickMultiply
7: LI R6, 2;            # Index of answer in RAM
8: SD R4, R6;           # Save answer to RAM
9: NOP;
10: AND R10, R1, R1;
11: LI R11, 123;
12: NOP;
13: NOP;
14: NOP;
15: END; 

## QuickMultiply 
16: LI R4, 0;           # Set ans, bit = 0, 1
17: LI R5, 1;

18: LI R6, 32;          # ID of first line after the loop
19: JLT R6, R3, R5;     # If b < bit, then exit loop
20: AND R7, R3, R5;     # b & bit
21: LI R6, 25;          # If (b & bit) != bit
22: JEQ R6, R7, R5;     #    then skip to 26 
23: LI R6, 26;          #    else add a to ans
24: JR R6;
25: ADD R4, R4, R2;     # ans += a
26: NOP;
27: ADD R2, R2, R2;     # a*= 2
28: ADD R5, R5, R5;     # bit *= 2
29: NOP;
30: LI R6, 18;          # going back to the beginning 
31: JR R6;              #    of the while loop

32: NOP;
33: LI R6, 6;           # Jump back in main 
34: JR R6;
