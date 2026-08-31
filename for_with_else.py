# l = [1, 5, 6, 8]
# for item in l:
#     print(item)

# else:
#     print("done")


# for i in range(101):
#     if(i == 101):
#         #break
#         continue
#     print(i)




#WAP to for with else function
def for_with_else(i):

    try:
        l = [1,3,2,5,9,8]
        for item in l:
            print(item)

        else:
            print("done")

        for i in range(101):
            if(i == 101):
                #break
                continue
            print(i)

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    for_with_else(101)