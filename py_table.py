#WAP to table
def print_table(i):

    try:
        i= 1
        n= int(input("enter number: "))
        while i <= 10:
            print(n*i)
            i += 1

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    print_table(8)