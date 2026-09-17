# #WAP to simple calculator
# print("""===simple calculator===""")

# num1=float(input("enter first number: "))
# num2=float(input("enter second number: "))

# print("\n select operation: ")
# print("1.Add")
# print("2.subtract")
# print("3.multiplication")
# print("4.divide")

# choice = input("enter choice: (1-4): ")

# if choice == '1':
#     print("Result:", num1+num2)

# elif choice == '2':
#     print("Result:", num1-num2)

# elif choice == '3':
#     print("Result:", num1*num2)

# elif choice == '4':
#      if num2 != 0:
#         print("Result: ",num1/num2)

#      else:
#         print("Error: Division by zero not allowed")


# else:
#     print("invalid choice: ")



#WAP to simple calculator
# def simple_calculator(i):
#     print("""===simple calculator===""")

#     num1=float(input("enter first number: "))
#     num2=float(input("enter second number: "))

#     print("\n select operation: ")
#     print("1.Add")
#     print("2.subtract")
#     print("3.multiplication")
#     print("4.divide")

#     choice = input("enter choice: (1-4): ")

#     try:
#         if choice == '1':
#          print("Result:", num1+num2)

#         elif choice == '2':
#          print("Result:", num1-num2)

#         elif choice == '3':
#          print("Result:", num1*num2)

#         elif choice == '4':
#          if num2 != 0:
#           print("Result: ",num1/num2)

#         elif choice == '5':
#          print("Error: Division by zero not allowed")

#         else:
#          print("invalid choice: ")

#     except Exception as e:
#        print("Error: ",e)

# if __name__ == "__main__":
#    simple_calculator(6)


# marks= [56,54,34,23,50,87,98]
# #       0, 1, 2, 3, 4, 5, 6,
# print(marks[1:6])

# # 
# list= ['c', 'a', 'd', 'b', 'g', 'z', 'x']
# print(list.sort())  
# print(list)


# tup= (1+2+3)/

# tup= (3,3,2,3,4,5,5,7,8,6,5)
# print(tup.count(7))

# movies= []
# mov1= input("enter 1st movie: ")
# mov2= input("enter 2nd movie: ")
# mov3= input("enter 3rd movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)



# list1= [1,2,1]
# List2= [1,2,3]


# copy_list1= list1.copy()
# copy_list1.reverse()

# if(copy_list1 == list1):
#     print("PALINDROME")

# else:
#     print("NOT PALINDROME")


# grade= ("P", "R", "I", "N", "C", "E", "P", "R", "P")
# print(grade.count("P"))


# grade= ["S","A","D","I","S","O","P","U","R"]
# grade.sort()
# # print(grade)

#WAP to print dictionary value 
# info= {
#     "name": "prince raj",
#     "subjects" : ["python", "java", "c"],
#     "topic" : ("dict", "set"),
#     "age" : 19
# }

# print(info["name"])
# print(info["subjects"])
# print(info["topic"])
# print(info["age"])


# collection= {1,2,2,2,3,"hello","prince","raj",4}
# print(collection)
# # print(type(collection))
# print(len(collection)) #total number of items

# collection= set() 
# print(type(collection))

# collection= set()
# collection.add(1)
# collection.add(2)
# collection.add("apna college")

# print(collection)

# set1= {1,2,3,4}
# set2= {2,3,4,5,4}

# print(set.intersection(set2))
# print(set1)
# print(set2)


# dictionary= {
#     "tiger": "a dengerous animal",
#     "table": ["a piece of furniture", "list of facts & figures"]
# }

# print(dictionary)

# subject= {
#     "python","java","c++","c","python","javascript","html","python"
# }

# print(subject)

# marks= { }

# x= int(input("enter phy: "))
# marks.update({"phy":x})


# x= int(input("enter che: "))
# marks.update({"che":x})


# x= int(input("enter math: "))
# marks.update({"math":x})

# print(marks)

# values= {"9",9.0}
# print(values)


# values= {
#     ("float", 9.0),
#     ("int",9)
# }
# print(values)


# def calc_sum(a, b):
#     sum= a + b
#     print(sum)
#     return sum

# calc_sum(34, 5)

# calc_sum(23, 7)

# calc_sum(67, 9)

# calc_sum(90, 7)

# calc_sum(87, 9)

# calc_sum(65, 7)

# calc_sum(89, 9)

# calc_sum(45, 7)

# calc_sum(12, 9)

# calc_sum(19, 7)

# # calc_sum(56, 9)

# #friction definition:
# def calc_sum(a, b): #parameters:
#     return a+b

# sum= calc_sum(1, 2) #function call; arguments
# print(sum)

# def print_hello():
#     print("hello")

# output= print_hello()
# print(output) #none


# #Average of 3 number
# def calc_avg(a,b,c):
#     sum = a + b + c
#     avg= sum/3
#     print(avg)
#     return avg

# calc_avg(1,2,3)


# print("hello", end= "$")  #sep= " "
# print("prince") #end= "\n"

# def cal_prod(a=4, b=6):
#     print(a * b)
#     return a*b

# cal_prod()

#WAP to print the length of a list. (list is the parameter)
cities= ["kolkata", "mumbai", "haryana","delhi","bhopal"]
heroes= ["ranveer kapoor", "salman khan", "sharu khan","akshya"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)