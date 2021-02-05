'''
This file contains the functions that you need for completing this assignment. 
1. expression_1() --> 30%
2. expression_2() --> 40%
3. expression_3() --> 30% 
Failure to follow the variable name guides will lead to reduction of 10 points. 
DO NOT EDIT THE FUNCTION NAMES.
'''

import math

def expression_1(x):
    calc_1 = ((2 * x) + (math.pow(x,2)))
    final_calc = math.pow(x,3) - calc_1 - 100
    print(f"x^3 - (2x + x^2) - 100 with the value of x as {x} equals {final_calc}")
expression_1(1)

def expression_2(x, y):
    calc_1 = (math.pow(x,4)/(2*y))
    calc_2 = (3 * (x * y))
    calc_3 = ((6*y)/(7*x))
    final_calc = int(calc_1 - calc_2 + calc_3)
    print(f"(x^4 / 2y) - (3xy) + (6y / 7x) with the value of x as {x} and y as {y} equals {final_calc}")
expression_2(1,2)

def expression_3(x, y):
    calc_1 = math.pow(x,3)
    calc_2 = math.pow(y,2)
    calc_3 = math.pow(x,2)
    calc_4 = math.pow(y,3)
    final_calc = (calc_1 + calc_2)/(calc_3 - calc_4)

    print(f"(x^3 + y^2) / (x^2 - y^3) with the value of x as {x} and y as {y} equals {final_calc}")
expression_3(1, 2)

if __name__ == "__main__":
    
    pass