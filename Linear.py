
# lst= [9,3,0,7,4,6]
# key = 6

# if key in lst:
#     print(lst.index(key))

# else:
#     print("not found")


#WAP to linear search
def linear_search(i):

    try:

        lst= [8,3,2,1,4,5,4,3]
        key= 3

        if key in lst:
            print(lst.index(key))

        else:
            print("not found")

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    linear_search(5)