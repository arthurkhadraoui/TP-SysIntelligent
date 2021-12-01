import random
from Army import Army
from Character import Character
import csv

characters_list=[]

with open (r'characters.csv',
           newline='') as csvfile:
    character = csv.reader(csvfile,delimiter=',',quotechar='|')
    rows = []
    header = next(character)
    for row in character:
        characters_list.append(Character(row[0],row[1],row[2],row[3],row[4]))

moralValue = random.uniform(20,100)
