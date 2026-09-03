
# #linear search
# lst = [10,23,46,56,87]
# key = 23.

# if key in lst:
#     print(lst.index(key))

# else:
#     print("not found")


#WAP to first repeating character
def linear_search(i):

    try:
        lst= [10,23,45,34,76,98]
        key= 76

        if key in lst:
          print(lst.index(key))

        else:
          print("Not found")

    except Exception as e:
       print("Error: ",e)

if __name__ == "__main__":
   linear_search(76)