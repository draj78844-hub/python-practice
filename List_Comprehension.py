# Adding 2 marks to each element using a normal for loop
# marks= [20, 40, 45, 89, 98]
# new_marks= [ ]
# for x in marks:
#     new_marks.append(x+2)

# print(new_marks)

#List Comprehension marks
# marks= [20, 40, 45, 89, 98]
# new_marks= [x+2 for x in marks]
# print(new_marks)

#normal for loop
# cubes= [ ]
# for x in range(10):
#     if x%2 == 0:
#       cubes.append(x ** 3)

# print("using for loop: ", cubes)


#List Comprehension cube
cube= [x ** 3 for x in range (10) if x%2 == 0]
print("Using List Coprehension: ", cube)