import pandas as pd

def main():
    arr_size = int(input('Please enter size of the dictionary: '))
    
    original_dict = {}
    for _ in range(arr_size):
        key = input('Enter the key: ')
        value = input('Enter the value: ')
        original_dict.update({key:value})
    
    print(f'Original dictionary:\n{original_dict}')
    
    s = pd.Series(original_dict)
    
    print('Converted series:')
    print(s)

main()