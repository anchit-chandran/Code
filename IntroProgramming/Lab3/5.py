def accept_login(users: dict, username: str, password: str):
    
    if users.get(username):
        if users[username] == password:
            return True 
    
    return False


users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
}

if accept_login(users, "user1", "password1"):
    print("login successful!")
else:
    print("login failed...")

assert accept_login(users, "user1", "password1") is True
assert accept_login(users, "user1", "wrongpassword") is False
assert accept_login(users, "wronguser", "password1") is False