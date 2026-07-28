# n = int(input("Enter a number: "))

# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     print("*" * (2 * i - 1))


#WAP to pyramid.
def pyramid(n):

    try:
        n= int(input("Enter a number: "))

        for i in range(1, n+1):
            print(" " * (n - i),end= "")
            print("*" *  (2 * i - 1))

    except Exception as e:
        print("Error: ",e)

pyramid(4)