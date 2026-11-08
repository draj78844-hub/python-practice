                                            #table print
# n= int(input("enter a number: "))
# for i in range(1, 11):
#     print(n * i)


                                            #even number to print 1 to 50
# for i in range(1, 51):
#     if i%2 == 0:
#         print(i)


                                            #odd number to print 1 to 50
# for i in range(1, 51):
#     if i%2 != 0:
#         print(i)

                                            #1 to 100 tak ka sum 
# total= 0
# for i in range(1,101):
#     total += i

# print(total)

                                            #1 to 5 table print
# for i in range(1, 6):
#     print(f"table of {i}")
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
#     print("---------")

                                            #star pattern
# for i in range(1, 11):
#     for j in range(i):
#         print("*", end=" ")

#     print()

                                            #reverse star pattern
# for i in range(16, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()




                                            # try except uses
# try:
#     num= int(input("enter an integer: "))
#     a= [6, 5]
#     print(a[num])

# except ValueError:
#     print("number entered is not an integer.")

# except IndexError:
#     print("index error")


# x= int("hello")
# print(x)

# x= int("3432")
# print(x)

# x= "hello"
# # x.capital()
# x.upper()

# x= [0] * 4
# # print(x)

# class first:
#     y= 199
# obj= first()
# print(obj.y)



# #WAP to print oops method
# class faculty:
#     def putdata(self):  #method 1
#         self.id= int(input("enter faculty id"))
#         self.name= input("enter name")
#         self.salary= float(input("enter faculty salary"))

#     def display(self):     #method 2
#         print("faculty id: ", self.id)
#         print("faculty name: ", self.name)
#         print("faculty salary: ", self. salary)

# a=faculty()
# a.putdata()
# a.display()


                                              #class & object method
# class Animal:
#       def sound(self): print("Animal sound")

# class Dog(Animal): pass

# d = Dog()
# d.sound()


# class person: 
#     name= "Prince Raj"
#     occupation= "Software engineer"
#     networth= 20
#     def info(self):
#         print(f"{self.name} is a {self. occupation}")


# a= person()
# a.info()

                                        #class & object method
class Details:
    name= input("enter a name: ")
    age= input("enter a age: ")

obj1= Details()
print(obj1.name)
print(obj1.age)

