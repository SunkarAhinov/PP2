import numpy as n
today = n.datetime64('today', 'D')
yesterday = n.datetime64('today', 'D') - n.timedelta64(1, 'D')
tomorrow =n.datetime64('today', 'D') + n.timedelta64(1, 'D')
print(today)
print(yesterday)
print(tomorrow)