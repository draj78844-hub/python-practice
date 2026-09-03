
#s = {1, 23, "prince", 9, 4}


#s.add(908)
#print(s,type(s))



# i = 1
# while i <= 10:
#     print(5 * i)
#     i += 1


#WAP to set and multiplication
def set(i):

    try:

        i= 1
        while i<= 10:
            print(5 * i)
            i += 1

    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    set(5)