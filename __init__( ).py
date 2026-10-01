# class test:
#     def __init__(self):
#         self.a= 8
#         self.b= 7

# t1= test()
# t2= test()
# print(t1.a,t1.b)
# print(t2.a,t2.b)





#Defining a node:

# class Node:
#     def __init__(self,item = None, next= None):
#         self.item = item
#         self.next = next

# #Node create krna

# node1 = Node(20)
# node2 = Node(56)

# node1.next = node2   # 👈 yahan connection ho raha hai

# print(node1.item)
# print(node1.next.item)


# class node://


# n.prev= None
# n.next= start 
# start.prev= n
# start= n



#GPT USES please try this 

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.prev = None
#         self.next = None


# # First node
# start = Node(10)

# # New node
# n = Node(5)

# # Insert n before start
# n.prev = None
# n.next = start
# start.prev = n
# start = n


# Display the doubly linked list
# temp = start

# while temp is not None:
#     print(temp.data)
#     temp = temp.next


#loops:---
#print numbers from 1 to 100
# i= 1
# while i <= 10:
#     print(i)
#     i += 1


#print numbers from 100 to 1
# i=100
# while i >= 1:
#     print(i)
#     i -= 1


#print the multiplication table of a number n
i= 1
while i <= 10:
    print(4*i)
    i+= 1
 
# print the elements of the following using a loop 
nums= [87, 54, 34, 78, 32, 98, 43]
print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])  
print(nums[4])


# nums= [67, 45, 23, 56, 34, 87, 67]

# #travers
# idx= 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1


# nums= (34, 56, 89, 65, 12, 98, 90, 23, 56)
# x= 23

# i=0
# while i < len(nums):
#     if(nums[i] == x):
#         print("FOUND at idx", i)
#     else:
#         print("finding")
#     i += 1


#loop...............................
# i= 1
# while i <= 6:
#     print(i)
#     if(i == 10):
#         break
#     i += 1
# print("end of loop")

# tup= (3,4,6,9,5,2)

# for num in tup:
# #     print(num)

# seq= range(201)
# for i in seq:
#     print(i)


#Factorial.......
# def calc_fact(n):
#     fact= 1
#     for i in range(1, n+1):
#         fact *=i

#     print(fact)

# calc_fact(7)

# def converter(usd_val):
#     inr_val= usd_val * 83
#     print(usd_val, "USD= ", inr_val, "INR")

# converter(0)

#Recursion.................
# def show(n):
#     if(n == 0): 
#         return
#     print(n)
#     show(n-1)

# show(45)

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
    print("END")

show(3)