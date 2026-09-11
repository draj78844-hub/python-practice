# class Student:
#      def __init__(self, name, marks, place):
#           self.name= name
#           self.marks= marks
#           self.place= place

#      print("adding new student in database...")

# s1= Student("prince", 98, "mumbai")
# print (s1.name, s1.marks, s1.place )

# s2= Student("aryan", 76, "bhopal")
# print(s2.name, s2.marks, s2.place)


# def welcome(self):
#     print("Welcome Student", self.name)


# class Student:
#     college_name= "BITS COLLEGE"


#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks

#     def welcome(self):
#         print("welcome student", self.name)

#     def get_marks(self):
#         return self.marks

# s1 = Student("prince", 88)
# s1.welcome()
# print(s1.get_marks())


#create student class that take name & mark of 3 sbject as argument in constructorthen create a method to print the average

# class student:

#     def __init__(self, name, marks):
#         self.name= name
#         self.marks= marks

#     @staticmethod #decorator
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum= 0 
#         for value in self.marks:
#             sum += value
#         print("hi", self.name, "your score is:", sum/3)

# s1= student("prince", [99,98,97])
# s1.get_avg()

# s1.name = "just_now"
# s1.hello()
# s1.get_avg()    



class car:

    def __init__(self):
        self.acc= False
        self.brk= False
        self.clutch= False

    def start(self):
        self.clutch= True
        self.acc= True
        print("car started..")

car1= car()
car1.start()


# class acc:

#     def __init__(self, bal, acc):
#         self.balance= bal
#         self.account_no= acc

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("total balance = ", self.get_balance())

#     def debit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("total balance = ", self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1= acc(20000, 12389)
# acc1.debit(1000)

# print(acc1.balance)
# # print(acc1.account_no)


# sum= 0
# while(True):
#     userInput= input("Enter the item price or press q to quit: \n")
#     if (userInput != 'q'):
#         sum= sum + int(userInput)
#         print(f"order total so far: {sum}")

#     else:
#         print(f"your bill total is {sum}. Thanks for shopping with us")
#         break

