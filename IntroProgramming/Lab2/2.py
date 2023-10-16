import math

def solution_2()->list[int]:
    
    # Constants
    X = 70
    H = 25
    
    nums = input('Please enter 3 integers, separated by commas, without whitespace: ')  
    
    Y = [int(num) for num in nums.split(',')]
    
    output = []
    
    for y in Y:
        numerator = 3 * X * y 
        denominator = H
        
        answer = str(round(math.sqrt((numerator / denominator))))
        
        output.append(answer)
    
    return ','.join(output)

print(solution_2())