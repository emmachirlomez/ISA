# This program multiplies 2 numbers. 

* Input: a in RAM(0) and b in RAM(1) 
* Output: the result of their product in RAM(2).

## Python equivalent code for mutiplying the 2 numbers:
```python
   def QuickMultiply(a, b):
       ans, bit = 0, 1
       while bit <= b:
           if (b & bit) == bit:
               ans += a
           a *= 2
           bit *= 2
       return ans
```

## Legend
* `R0` = 0
* `R1` = 1
* In `QuickMultiply`, we will use: 
  * `R2` = a
  * `R3` = b
  * `R4` = ans
  * `R5` = bit