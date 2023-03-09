def is_armstrong_number(number):
    return (number == (sum([int(n) ** len(str(number)) for n in str(number)]))) if number >= 0 else False 

        
    
    
    
