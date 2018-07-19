from random import choice
from string import ascii_uppercase

def check():
    return True

def make_grid(row, column):
    grid = {}
    
    for r in range(row):
        for c in range(column):
            grid[(r, c)] = choice(ascii_uppercase)
   
    return grid
    
print(make_grid(2, 2))