# for i in range(10):    #range(stop)
#     print(i) 
# for i in range(2, 20):    #range(start, stop)
#    print(i)

# for i in range(2, 100, 10):   #range(start, stop, step)   
#    print(i)

# for i in range(2, 100, 2):     #even number
#     print(i)    
# for i in range(1, 100, 2):      #odd numb   
#     print(i for i in range(100, 0, -1))    
#     print(i)

# #WAP to start, stop and step
# def start_stop(i):

#     try:

#         for i in range(10):    
#             print(i) 

#         for i in range(2, 20):    
#             print(i)

#         for i in range(2, 100, 10):    
#             print(i)

#         for i in range(2, 100, 2):    
#             print(i) 

#         for i in range(1, 100, 2):      
#             print i in range(100, 0, -1)    
          
#         print(i)

#     except Exception as e:
#         print("Error: ",e)

# if __name__ == "__main__":
#     start_stop(int)




# WAP to start, stop and step
def start_stop():

    try:
        print("0 to 9:")
        for i in range(10):
            print(i)

        print("2 to 19:")
        for i in range(2, 20):
            print(i)

        print("2 to 99 with step 10:")
        for i in range(2, 100, 10):
            print(i)

        print("2 to 98 with step 2:")
        for i in range(2, 100, 2):
            print(i)

        print("Odd numbers:")
        for i in range(1, 100, 2):
            print(i)

        print("Reverse counting:")
        for i in range(100, 0, -1):
            print(i)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    start_stop()