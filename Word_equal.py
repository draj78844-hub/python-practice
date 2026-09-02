
# #check if two string are equal
# s1 = input()
# s2 = input()

# if s1 == s2:      
#     print("equal")

# else:
#     print("not equal")


#WAP to string are equal
def word():

    try:

        s1= input()
        s2= input()

        if s1 == s2:
            print("Equal")

        else:
            print("Not Equal")


    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    word()