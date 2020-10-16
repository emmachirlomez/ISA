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

### Potential use

Multiplying to polinomials.
In other words, simulate this code:
```python
def multiply(a, b):
    ans = [0 for i in range(len(a) + len(b))]
    for i in range(len(a)):
        for j in range(len(b)):
            ans[i + j] += a[i] * b[j]
    return ans
```