# l = ["prince", "deep", "ladoo", "pugu"]
# name = input("enter your name: ")

# if(name in l):
#     print("your name is in the list")

# else:
#     print("your name is not in the list")

#WAP to name list
def entered_list(l):

    try:
        name= input("enter your name: ")
        if(name in l):
            print("your name is in the list")

        else:
            print("your name is not in the list")

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    entered_list("prince, deep, ladoo, pugu")