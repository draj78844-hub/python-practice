
# #number pattern
# n = 10
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j,end= " ")

#     print()



def number_pattern(i):
    try:
        n=10
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j,end=" ")

            print()

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    number_pattern(45)