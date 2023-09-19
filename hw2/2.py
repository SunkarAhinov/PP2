str="";
for row in range(0,7):
    for column in range(0,7):
        if(column==1):
            str=str+"*"
        elif((row==0 or row==3) and column>1 and column<5):
            str=str+"*"
        elif(column==5 and row != 0 and row<3):
            str=str+"*"
        elif(column == row-1 and row>2):
            str=str+"*"
        else:
            str=str+" "
print(str);


str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if(column==1):  
            str=str+"*" 
        elif((row==0 or row==3) and column>1 and column<5):
            str=str+"*"
        elif(column==5 and row != 0 and row<3):
            str=str+"*"
        elif(column == row-1 and row>2):
            str=str+"*"
        else:      
            str=str+" "    
    str=str+"\n"    
print(str);