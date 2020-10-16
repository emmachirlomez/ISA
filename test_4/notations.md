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

## Using this function for multipliying stuff elsewere

This function **IS NOT MADE** for being used elsewere.
However, the recomended way to do it if you really want to is:
* Change the registers used by the function to be some predefined, temporary registers.
* Send the values of `a` and `b` as two predefined registers, one of which could be used to store the answer (for instance, `a`'s register).
* Also store the address the function was called from in another register, and make the `QuickMultiply` function jump back there.

### Potential uses

* Exponentiation in logaritmic time with multiplications
* Multiplying a polinomial by a constant (although should keep in mind the 255 lines limit)