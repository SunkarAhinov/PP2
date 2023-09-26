def myfunc(wlist):
    wlen = []
    for i in wlist:
        wlen.append((len(i), i))
    wlen.sort()
    return wlen[-1][0], wlen[-1][1]
result = myfunc([input(),input(),input()])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])