# username = input("enter username: ")

# if(len(username)<10):
#     print("your username contain less than 10 character")

# else:
#     print("all is well")

#WAP to len of username
def len_username(s):

    try:
        username= input("Enter username: ")

        if(len(username)<10):
            print("your username contain less than 10 character")

        else:
            print("All is well")

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    len_username("prince raj")