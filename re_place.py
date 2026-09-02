# word = "Donkey"

# with open("file.txt","r") as f:
#    content = f.read()

# contentnew = content.replace(word, "######")

# with open("file.txt", "w") as f: 
#     f.write(contentnew)

# print("file updated successfully")



#WAP to word replace
def re_place(s):

    try:
        word= " "
        with open("file.txt", "r") as f:
            content= f.read()

        contentnew= content.replace(word, "######")

        with open("file.txt", "w") as f:
            f.write(contentnew)

        print("file updated successfully")

    except Exception as e:
        print("Error: ",e)


if __name__ == "__main__":
    re_place("Donkey")