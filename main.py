#READING A FILE 
# f= open('myfile.txt','r')
# # print(f)
# text= f.read()
# print(text)
# f.close()

#WRITING A FILE
# f= open('myfile.txt', 'a')
# f.write('Hello, Prince Bhai!')
# f.close()

#EASY METHOD WRITING A FILE KA 
with open('my file.txt', 'a')as f:
    f.write("Hey i am inside with")