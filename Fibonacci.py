# #WAP to fibonacci series
# n = int(input("enter number of terms: "))
# a = 0
# b = 1
# for i in range(n):
#     print(a, end=" ")
#     c = a+b
#     a = b
#     b = c 


#WAP to fibonacci series
def fibonacci_series(i):

    try:
        n= int(input("enter number of terms: "))
        a= 0
        b= 1

        for i in range(n):
            print(a, end= " ")
            c= a+b
            a= b
            b= c

    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    fibonacci_series(6)