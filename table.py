# n = int(input("enter a number: "))

# for i in range(1, 11):
    
#      print(f"{n} * {i} = {n * i}")


#WAP to multiple sign uses in table.
def multiple_signtable(i):
     n= int(input("enter a number: "))

     try:
          for i in range(1, 11):
               print(f"{n} * {i} = {n * i}")

     except Exception as e:
          print("Error: ,e")

if __name__ == "__main__":
     multiple_signtable(5)
