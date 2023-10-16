"""Write a function that evaluates the mathematical functions
 Return these three values. Write out the results of these values for x = Pi."""
import math
def solution_3():
    x = math.pi
    fn_1 = math.cos(x)
    fn_2 = -2 * math.sin(2*x)
    fn_3 = -4 * math.cos(2*x)
    
    return fn_1, fn_2, fn_3

print(solution_3())
