
#     [6]prime number check
# n = int(input("enter a number: "))
# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count += 1

# if count == 2:
#     print("prime number")      

# else:
#     print("not a prime number") 


#WAP to prime number
def prime(i):

    try:

        n= int(input("Enter a number: "))
        count= 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1

        if count == 2:
                print("Prime Number")

        else:
                print("Not Prime Number")


    except Exception as e:
        print("Error: ",e)


if __name__ == "__main__":
    prime(6)