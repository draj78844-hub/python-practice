
# a = int(input())
# b = int(input())

# a,b = b,a
# print(a)
# print(b)

#WAP to swap variable
def swap(i):

    try:
        a= int(input())
        b= int(input())

        a,b = b,a

        print(a)
        print(b)

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    swap(4)