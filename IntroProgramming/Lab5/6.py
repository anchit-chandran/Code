import numpy as np

def main():
    arr_size = int(input('Please enter size of the array:'))
    
    arr = np.array([int(input('Enter element: ')) for _ in range(arr_size)])
    
    print(f'Test array: {arr}')
    print(f'Test if none of the elements of the said array is zero: {np.all(arr)}')

main()