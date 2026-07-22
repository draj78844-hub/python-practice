# #using break loop:
# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)

 

def break_loop(i):

    try:
        for i in range(1, 11):
            if i == 7:
                break

            print(i)

    except Exception as e:
        print("Error: ",e)

if __name__== "__main__":
    break_loop(6)