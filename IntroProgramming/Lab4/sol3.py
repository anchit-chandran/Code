import random

from sol2 import Robot1

class Robot2(Robot1):
    
    def __init__(self):
        self.available_sayings = ['BEEP BEEP Default']
        super()
    
    def set_sayings(self, new_sayings:list)->None:
        self.available_sayings = new_sayings
    
    def speak(self)->None:
        print(random.choice(self.available_sayings))

rb2 = Robot2()
rb2.set_sayings(['Exterminate, exterminate!', 'I obey', 'Am I conscious?', 'Can you prove that you are conscious?'])
rb2.speak()