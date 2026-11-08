#WAP to print nested for loop
for i in range(1, 6):
    for j in range(1, 7):
       for p in range(1, 8):
           for m in range(1, 9):
               for x in range(1, 10):
                   for a in range(1, 11):
                       for num in range(1, 12):
                           print(num)



#WAP to print nested while loop
counter= 1
while counter <= 11:
    num= 1
    while num <= 5:
        print(num)
        num= num+1

    counter= counter+1



#This code in just 3 lines that prints multiplication tables from 1 to any number.
for i in range(2, 15):
    for j in range(1, 11):
        print(i,"*", j, "=", i*j)