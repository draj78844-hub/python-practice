
# #anagram
# s1= input()
# s2= input()

# if sorted(s1) == sorted(s2):
#     print("anagram")

# else:
#     print("not anagram")



#WAP to anagram 
def anagram():
    try:

        s1= input()
        s2= input()

        if sorted(s1) == sorted(s2):
         print("Anagram")

        else:
         print("not anagram")

    except Exception as e:
       print("Error: ",e)

if __name__ == "__main__":
   anagram()