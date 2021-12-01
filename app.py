from Character import Character
import csv

characters_list=[]

with open (r"characters.csv",
           newline='') as csvfile:
    character = csv.reader(csvfile,delimiter=';',quotechar='|')
    rows = []
    for row in character:
        rows.append(row)

