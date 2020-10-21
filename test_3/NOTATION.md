- R0 = Fixed 0
- R1 = Fixed 1
- R2 = Soubroutine to run
  - 1 - ADD
  - 2 - SUB
  - 3 - MULC
  - 4 - MUL
  - 5 - MULX
  - 6 - EVAL
- R3-9 are temporaries
- R10 - start of p1
- R11 - length of p1
- R12 - start of p2
- R13 length of p2
- R14,15 are temporaries
- Polinomials are stored in continous chuncks in memory (Starting from R10 / R12)

-------------------
EMMA: MUL and MULC
DUSANA: ADD and sub
PAulo: Eval mul X