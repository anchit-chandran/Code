def solution_5(candidate_string):
    start, end = 0, -1

    for _ in range(len(candidate_string) // 2):
        if candidate_string[start] != candidate_string[end]:
            print("Not a palindrome")
            return False

        start += 1
        end -= 1
        
    return True


print(solution_5("racecar"))
assert solution_5("racecar") == True