# str = "i am studying from python"
# print(str.find("p"))

def letter_number():

    try:
        str= "i am studying from python"
        print(str.find("i"))

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    letter_number()