

# def factorial(n):

#     try:
#         n= int(input("enter a number: "))

#         for i in range(1, 11):
#             print(f"{n} * {11 - i} = {n *(11 - i)}")

#     except Exception as e:
#         print("Error: ",e)

# if __name__ == "__main__":
#     factorial(n)





#WAP to print factorial...........
def factorial(n):
    try:
        result = 1

        for i in range(1, n + 1):
            result *= i

        print(f"Factorial of {n} = {result}")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    factorial(n)