# #rotate list
# lst = [1,2,3,4,5]
# k = 2

# print(lst[k:] + lst[:k])

# #WAP to rotate list
def rotate_list(l):

    try:
        k = 2
        print(l[k:] + l[:k])

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    rotate_list([1,2,3,4,5])