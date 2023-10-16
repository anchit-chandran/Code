def solution_4(list_a:list, list_b:list):
    
    list_a, list_b = set(list_a), set(list_b)
    
    unique_common_elements = list_a.intersection(list_b)
    
    return list(unique_common_elements)

list_a = [5, 23, 7, 89,7, 90]
list_b = [89, 25, 89, 7, 14, 76, 5, 11, 5]

print(solution_4(list_a, list_b))