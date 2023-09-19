human_age = float(input("Input a dog's age in human years: "))
dog_age = 0
if(human_age>2):
    dog_age=(human_age-2)*4+2*10.5
elif(human_age<=2):
    dog_age=human_age*10.5
else:
    dog_age="error"
print("The dog's age in dog's years is" ,dog_age)