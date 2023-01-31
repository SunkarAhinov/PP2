hour1=int(input())
minute1=int(input())
second1=int(input())

hour2=int(input())
minute2=int(input())
second2=int(input())

sec=60

S1=hour1*sec*sec+minute1*sec+second1

S2=hour2*sec*sec+minute2*sec+second2

if S1>S2:
      print(S1-S2)
else:
      print(S2-S1)