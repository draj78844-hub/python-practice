#percentage of marks
# marks1 = int(input("Enter marks1: "))
# marks2 = int(input("Enter marks2: "))
# marks3 = int(input("Enter marks3: "))

# # check total percentage
# total_percentage = (100 * (marks1 + marks2 + marks3)) / 300

# if total_percentage >= 40 and marks1 > 33 and marks2 > 33 and marks3 > 33:
#     print("You are passed:", total_percentage)
# else:
#     print("You failed, try again next year:", total_percentage)


#WAP to percentage in marks
def percentage():

    try:
        marks1 =int(input("Enter marks1: "))
        marks2 =int(input("Enter marks2: "))
        marks3 =int(input("Enter marks3: "))

        #check total percentage 
        total_percentage= (100 * (marks1 + marks2 + marks3)) / 300

        if total_percentage >= 40 and marks1 > 33 and marks2 > 33 and marks3 > 33:
            print("you are passed: ",total_percentage)

        else:
            print("you failed, try again next year: ", total_percentage)

    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    percentage()