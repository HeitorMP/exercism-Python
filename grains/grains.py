def square(number):
    if number not in range(1,65): raise ValueError("square must be between 1 and 64")
    return (square(number - 1) * 2) if number > 1 else 1

    
    


def total():
    return square(64) * 2 - 1
