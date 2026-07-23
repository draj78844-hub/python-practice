# n = int(input("enter a number: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 2

#WAP to natural number
def natural_num(i):

    try:
        n= int(input("enter a number: "))
        i = 1
        while i <= n:
            print(i)
            i += 2

    except Exception as e:
        print("Error: ")

if __name__ == "__main__":
    natural_num(7)