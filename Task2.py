"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
duration_Max= 0
dic = {}
for caller, receiver, time, duration in calls:
    if caller in dic:
        dic[caller]+=duration
    elif caller not in dic:
        dic[caller] = duration

    if receiver in dic:
        dic[receiver]+=duration    
    elif receiver not in dic:
        dic[receiver] = duration    
caller_Max= max(dic)
duration_Max = dic[max(dic)]
print(caller_Max, 'spent the longest time,', duration_Max, "seconds, on the phone during September 2016.") 