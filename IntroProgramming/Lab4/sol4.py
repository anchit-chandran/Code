from datetime import date

class CreditCard:
    
    def __init__(self, expiry_month:int, expiry_year:int, first_name:str, last_name:str, cc_number:str):
        
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.first_name = first_name
        self.last_name = last_name
        self.cc_number = cc_number
    
    def format_expiry_date(self)->str:
        
        return f'{self.expiry_month}/{str(self.expiry_year)[2:]}'

    def format_full_name(self)->str:
        return f'{self.first_name} {self.last_name}'
    
    def format_cc_number(self)->str:
        
        return f'{self.cc_number[:4]} {self.cc_number[4:8]} {self.cc_number[8:12]} {self.cc_number[12:]}'
    
    def is_valid(self)->bool:
        current_date = date.today()
        card_expiry_date = date(year=self.expiry_year, month=self.expiry_month, day=current_date.day)
        
        return current_date < card_expiry_date
    
    def __str__(self):
        
        return f"Number: {self.format_cc_number()} Expiry date: {self.format_expiry_date()} Account holder: {self.format_full_name()} Is valid: {self.is_valid()}"
    

cc1 = CreditCard(10, 2014, 'bob','jones','1234567890123456')
print(cc1)

cc2 = CreditCard(12, 2030, 'bob','jones','1234567890123456')
print(cc2)