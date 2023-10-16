from collections import Counter

def solution_6(words: list):
    return list(Counter(words).most_common())


words = [
    "London",
    "Oslo",
    "Paris",
    "Rome",
    "Paris",
    "Geneva",
    "Paris",
    "Milano",
    "Geneva",
    "Paris",
    "Granada",
    "Rome",
    "Rome",
    "London",
    "London",
    "Geneva",
    "Geneva",
    "Oslo",
    "Rome",
    "Oslo",
    "Oslo",
    "Rome",
    "Oslo",
    "Rome",
    "Geneva",
    "Granada",
    "Granada",
    "London",
]

print(solution_6(words))