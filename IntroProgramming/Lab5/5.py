class UsernameNotUniqueException(Exception):
    def __init__(self, username, message='Username is not unique'):
        self.message = message if not username else f'{username=} is not unique'
        return super().__init__(self.message)

class AgeNotPositive(Exception):
    def __init__(self, age, message='Age must be positive') -> None:
        self.message = message if not age else f'Invalid age: {age}'
        super().__init__(self.message)

class Underage(Exception):
    def __init__(self, username, message='')->None:
        self.username = username
        super().__init__(f'{self.username=} is underage')

class InvalidEmail(Exception):
    def __init__(self, email):
        self.email = email
        super().__init__(f'\'{self.email}\' is not a valid email address.')

usersList = [
    ("jane", "jane@example.com", 21),
    ("bob", "bob@example", 19),
    ("jane", "jane2@example.com", 25),
    ("steve", "steve@somewhere", 15),
    ("joe", "joe", 23),
    ("anna", "anna@example.com", -3),
]

    
def main(usersList):
    
    usernames = []
    for data in usersList:
        
        try:
            # check username unique
            if data[0] not in usernames:
                usernames.append(data[0])
            else:
                raise UsernameNotUniqueException(username=data[0])
            
            # age pos check
            if data[-1] < 0:
                raise AgeNotPositive(age=data[-1])
            
            # underage
            if data[-1] < 15:
                raise Underage(username=data[1])
            
            # email 
            email_check = data[1].split('@')
            if (len(email_check)!= 2) or (not email_check[0]) or (not email_check[1]):
                raise InvalidEmail(email=data[1])
        
        except UsernameNotUniqueException as unq:
            print(unq)
        except AgeNotPositive as anp:
            print(anp)
        except Underage as ua:
            print(ua)
        except InvalidEmail as ie:
            print(ie)
        

main(usersList)