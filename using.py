# #WAP to list using a loop
# nums = [88, 98, 76, 95, 67, 78]
# god = ["hanuman", "sankar", "maa", "bholenath"]

# i = 0
# while i < len(god):
#     print(god[i])
#     i += 1


#WAP to using loop
def using_loop(s):

    try:
        
        god= s.split(", ")

        i = 0
        while i < len(god):
            print(god[i])
            i += 1

    except Exception as e:
        print("Error: ")

if __name__ == "__main__":
    using_loop("hanuman, sankar, god")