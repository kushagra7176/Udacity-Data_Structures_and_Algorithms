"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
dic = {}
count = 0
for caller, receiver, time in texts:
    if caller not in dic:
        dic[caller] = count
        count+=1
    if receiver not in dic:
        dic[receiver] = count
        count+=1

for caller, receiver, time, duration in calls:
    if caller not in dic:
        dic[caller] = count
        count+=1
    if receiver not in dic:
        dic[receiver] = count
        count+=1        

print('There are', count, ' different telephone numbers in the records')