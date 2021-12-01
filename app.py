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
        characters_list.append(Character(row[0],row[1],int(row[2]),row[3],float(row[4])))

armys = []

for character in characters_list:
    armys.append(Army(character,random.uniform(20,100)))


valeurTotaleArmee=0
for armee in armys:
    print("Armée de "+ armee.getChief().getPrenom()+": "+str(armee.get_total_moral()))