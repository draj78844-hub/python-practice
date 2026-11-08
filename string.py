# name = "prince"

# print(len(name))
# print(name.endswith("ce"))
# print(name.startswith("pri"))
# print(name.capitalize())


#WAP to name different types pattern
# def string_operation():
#     try:
#         name= "prince"

#         print(len(name))
#         print(name.endswith("ce"))
#         print(name.startswith("ra"))
#         print(name.capitalize())

#     except Exception as e:
#         print("Error: ",e)

# if __name__ == "__main__":
#     string_operation()




name= "prince raj"
friend= "krishna"
pomegranate= '''He said,
            hlo prince
            how are you
            what are you going
            i want to eat a pomegranate'''

print("hello, " + name)
# print(pomegranate)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])
print(name[8])
print(name[9])
# print(name[10]) throws an error
print("lets use a for loop\n ")
for character in pomegranate:
    print(character)