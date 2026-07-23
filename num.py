#WAP to print 1 to 100 num:
# i = 100
# while i >= 1:   #this is a stopping value
#     print(i)
#     i -= 1

#WAP to print 1 to 100 num:
def counting_num(i):

    try:
        while i >= 1:
            print(i)
            i -= 1

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    counting_num(100)