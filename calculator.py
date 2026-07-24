# #WAP to simple calculator
# print("""===simple calculator===""")

# num1=float(input("enter first number: "))
# num2=float(input("enter second number: "))

# print("\n select operation: ")
# print("1.Add")
# print("2.subtract")
# print("3.multiplication")
# print("4.divide")

# choice = input("enter choice: (1-4): ")

# if choice == '1':
#     print("Result:", num1+num2)

# elif choice == '2':
#     print("Result:", num1-num2)

# elif choice == '3':
#     print("Result:", num1*num2)

# elif choice == '4':
#      if num2 != 0:
#         print("Result: ",num1/num2)

#      else:
#         print("Error: Division by zero not allowed")


# else:
#     print("invalid choice: ")



#WAP to simple calculator
def simple_calculator(i):
    print("""===simple calculator===""")

    num1=float(input("enter first number: "))
    num2=float(input("enter second number: "))

    print("\n select operation: ")
    print("1.Add")
    print("2.subtract")
    print("3.multiplication")
    print("4.divide")

    choice = input("enter choice: (1-4): ")

    try:
        if choice == '1':
         print("Result:", num1+num2)

        elif choice == '2':
         print("Result:", num1-num2)

        elif choice == '3':
         print("Result:", num1*num2)

        elif choice == '4':
         if num2 != 0:
          print("Result: ",num1/num2)

        elif choice == '5':
         print("Error: Division by zero not allowed")

        else:
         print("invalid choice: ")

    except Exception as e:
       print("Error: ",e)

if __name__ == "__main__":
   simple_calculator(6)

