import csv

listFromShortXss = []
listFromLongXss = []
listFromSQL = []

with open('shortXss.csv','r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        listFromShortXss.extend(row)

with open('longXss.csv','r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        listFromLongXss.extend(row)

with open('SQL.csv','r',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        listFromSQL.extend(row)