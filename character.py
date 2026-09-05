
   
# #character occurence
# s = input("enter string: ")
# ch = input("enter character: ")

# count = s.count(ch)
# print(count)



#WAP to character occurance
def character(s):

    try:
        s= input("Enter string: ")
        ch= input("Enter character: ")

        count= s.count(ch)
        print(count)

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    character("hello")

