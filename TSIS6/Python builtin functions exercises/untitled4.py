def multi(numbers):  
    t = 1
    for x in numbers:
        t *= x  
    return t  
print(multi((8, 2, 3, -1, 7)))