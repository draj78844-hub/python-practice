# a = int(input("enter your number: "))
# print("the square of the number is", a*a)

# square=lambda x:x*x

def square_number(i):

    try:
        a= int(input("enter your number: "))
        print("the square of the number is", a*a)
        square= lambda x:x*x

    except  Exception as e:
        print("Error: ",e)


if __name__ == "__main__":
    square_number(5)

