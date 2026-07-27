# import random
# import string

# randNum = random.radint(1, 5)
# print(randNum) 


#WAP to random number.
def random_num(i):

    try:
        import random
        import string

        randNum = random.randint(1, 20)
        print(randNum)

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    random_num(15)