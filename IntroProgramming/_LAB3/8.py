from datetime import date
from dateutil.relativedelta import relativedelta

def dates_generator(start_date, end_date):
    
    while start_date <= end_date:
        
        yield start_date
        
        start_date += relativedelta(days=1)

def solution_8():
    startDate = date(2025, 4, 27)
    endDate = date(2025, 5, 7) 
    
    for day in dates_generator(start_date=startDate, end_date=endDate):
        print(day)
    
    

solution_8()