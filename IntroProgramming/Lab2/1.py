def solution_1()->None:
    for i in range(2000,4001):
        if ((i % 9) == 0) and not ((i % 2) == 0):

            print(i, end=',')

solution_1()
