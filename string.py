# name = "prince"

# print(len(name))
# print(name.endswith("ce"))
# print(name.startswith("pri"))
# print(name.capitalize())


#WAP to name different types pattern
def string_operation():
    try:
        name= "prince"

        print(len(name))
        print(name.endswith("ce"))
        print(name.startswith("ra"))
        print(name.capitalize())

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    string_operation()