#WAP to armstrong number
n= int(input())
temp = n
sum= 0

while n > 0:
    digit = n % 10
    sum += digit **3
    n//= 10

if temp == sum:
    print("armstrong")

else:
    print("not armstrong")