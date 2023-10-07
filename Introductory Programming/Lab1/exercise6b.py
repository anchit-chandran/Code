def verify_password(user_input:str)->str:
    """Verify user password is same as defined.

    Args:
        user_input (str): the user input 

    Returns:
        str: message stating success
    """
    
    password = '123'

    if user_input == password:
        print('Password accepted!')
    else:
        print('Wrong password')

user_input = input('Please enter the password: ')

verify_password(user_input)