
#need this variable to get the user to input a starting range
range1 = input("Please choose a number to start your range: ")

#need this variable to get the user to input an ending range
range2 = input("Please choose a number to end your range: ")

i = 0
#need this variable for a counter

j = 0
#need this variable for a counter

flag = 0
#need this variable to know if value is prime or not
if int(range1) <= 1:
    print('Please make your starting number greater than 1')
if int(range2) <= int(range1):
    print('Please make sure the ending number is greater than starting number')

for i in range(int(range1),int(range2)+1):
    if (i == 1):
        continue
    flag = 1
    for j in range(2,i//2+1):
        if(i%j == 0):
            flag = 0
            break
    if (flag == 1):
        print(i,end="\n ")
