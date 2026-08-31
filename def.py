# #def show(n):
#    # if(n == 0):
#    #     return 
#    # print(n)
#   #  show(n -  1)

# #show(10)


# #def fact(n):
#  #   if(n == 1 or n == 0):
#  #       return 1
#  #   return fact(n - 1) * n

# #print(fact(6))


# def print_list(list, idx=0):
#     if (idx == len(list)):
#         return
#     print(list[idx])
#     print_list(list, idx+1)


# fruits =["mango", "papaya", "orange", "black berry", "guava", "litchi"]
# print_list(fruits)


def print_list(items, idx=0):

    try:
        if idx == len(items):
            return
        
        print(items[idx])
        print_list(items, idx + 1)

    except Exception as e:
        print("Error: ,e")

if __name__ == "__main__":
    print_list(["mango", "papaya", "coconut", "kiwi", "guava", "apple"])