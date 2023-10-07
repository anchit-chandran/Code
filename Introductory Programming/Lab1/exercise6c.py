def calculate_ucl_grade(average_grade: int)->str:
    """Returns grade as string depending on mark.

    Args:
        average_grade (int): the average module mark. Assumed to be between 0-100 inclusive.

    Returns:
        str: the grade, from one of ['Distinction', 'Pass', 'Fail']
    """
    if average_grade >= 70:
        print('Distinction')
    elif 50 <= average_grade <= 69:
        print('Pass')
    else:
        print('Fail')

average_mark = int(input('Please enter your average mark for the module: '))

calculate_ucl_grade(average_mark)