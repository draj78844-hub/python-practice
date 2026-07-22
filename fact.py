# n = int(input("enter number: "))
# fact = 1

# for i in range(1, n+1):
#     fact *= i

# print("factorial= ", fact)


#WAP to print factorial
def print_factorial(i):

    try:
        n= int(input("enter number: "))
        fact= 1
        for i in range(1, n+1):
            fact *= i

        print("factorial= ",fact)

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    print_factorial(12)