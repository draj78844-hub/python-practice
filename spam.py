# p1 = "make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"

# message = input("enter your comment: ")
# if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
#     print("this comment is a spam")

# else:
#     print("this comment is not a spam")

#WAP to print spam comment...
def spam_comment(s):

    try:
        p1= "make a lot of money"
        p2= "buy now"
        p3= "subscribe this"
        p4= "click this"

        message= input("enter your comment: ")
        if(p1 in message) or (p2 in message) or (p3 in message) or (p4 in message): 
            print("this comment is a spam")

        else:
            print("this comment is not a spam")

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    spam_comment(2)