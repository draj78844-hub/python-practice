# l1 = [1, 54, 76,32,23,12,89,90]
# #l1.sort()
# #l1.reverse()
# #l1.insert(3,333)
# value = l1.pop(3)
# print(value)
# print(l1)



#WAP to list method in reverse terms.
def list_method(i):

    try:
        l1= [23, 45, 34, 65, 44, 33]
        l1.reverse()
        print(l1)

    except Exception as e:
        print("Error: , e")

if __name__ == "__main__":
    list_method(4)