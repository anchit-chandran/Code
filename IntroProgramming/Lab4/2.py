class Robot1:
    
    def __init__(self):
        self.battery_charge = 5.0
    
    def move(self, distance: int)->None:
        
        while distance > 0:
            print(f'Current charge: {self.battery_charge}')
            if self.battery_charge <= 0.5:
                print(f'Not enough charge remaining: {self.battery_charge=}')
                break
            
            self.battery_charge -= 0.5
            distance -= 1
            print(f'Moved 1 unit, consuming charge.')
        
        
        
    
    def battery_charge(self, charge:float)->None:
        """Increments `battery_charge` instance attribute by `charge` amount.

        Args:
            charge (float): amount to add to current charge
        """
        
        self.battery_charge += charge

rb = Robot1()
rb.move(11)
rb.move(11)