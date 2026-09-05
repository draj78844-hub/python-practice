
#      [9]palindrome check
# n = int(input("Enter a number: "))
# temp = n
# rev = 0

# while n > 0:
#     rev = rev*10 + n%10
#     n //=10
# if temp == rev:
#     print("Palindrome")

# else:
#     print("Not Palindrome")


#WAP to palindrome
def palindrome(i):

    try:
        n= int(input("Enter a number: "))
        temp= n
        rev= 0

        while n > 0:
            rev= rev*10 + n%10
            n //= 10
        if temp == rev:
             print("Palindrome")

        else:
             print("Not Palindrome")

    except Exception as e:
        print("Error: ")


if __name__ == "__main__":
    palindrome(10)