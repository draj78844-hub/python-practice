# class A:
#     varA = "welcome to class A"

# class B:
#     varB = "welcome to class B"

# class C(A,B):
#     varC = "welcome to class C"

# c1 = C()

# print(c1.varA)
# print(c1.varB)
# print(c1.varC)


#WAP to inheritance
def inheritance():

    try:
        class A:
            varA = "Welcome to class A prince babu"

        class B:
            varB = "Welcome to class B b tech course"

        class C(A, B):
            varC = "Welcome to class C welcome in my house"

        c1 = C()

        print(c1.varA)
        print(c1.varB)
        print(c1.varC)

    except Exception as e:
        print("Error: ", e)

if __name__ == "__main__":
    inheritance()

         