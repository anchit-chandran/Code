import re
from operator import itemgetter

def get_input()->tuple[str, int, int]:
    
    player_input = input('Please enter all players\' data in the following format:\n\n(\'NAME\', AGE, SCORE)\n\nReplace capitalised words with the actual value and separate each item with a comma\n\ne.g. (\'Anchit\', 25, 10),(\'Anchit\', 25, 10)\n\nWRITE DATA: ')

    data = []
    regex_pattern = r"\('\w+',\d+,\d+\d\)"
    for item in re.findall(regex_pattern, player_input):
        item_cleaned = item.replace('(','').replace(')','').replace('\'','').split(',')
        data.append(
            (item_cleaned[0], int(item_cleaned[1]), int(item_cleaned[2]))
        )
    
    return data
    

def solution_3(player_data):
    sorted_data = sorted(player_data, key=itemgetter(0,1,2))
    return sorted_data

# ('John',20,80),('Jony',19,95),('Anna',18,70),('Json',23,120)
player_data = get_input()
print(solution_3(player_data=player_data))