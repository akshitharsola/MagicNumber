
#n=int(input("Enter your 3 digit number: "))
n=int(input())
#n=356
print("The number you provided is 👇")
print(n)
print("First step is reverse the given number..")
t=n
r=0
while(t!=0):
    a=t%10
    r=r*10+a
    t//=10
#print(n)
print("And the number is 👇")
print(r)
print("Now subtract original number and reversed number..")
print("And the output is 👇 ")
first= n-r
if(first < 0):
    first = abs(n-r)
    print(first)
else:
    print(first)
print("NOTE: If your output is in negative then just change it to positive")
print("Second step is the output we have reverse it")
print("And that is 👇")
b=first
c=first
s=0
while(c!=0):
    d=c%10
    s=s*10+d
    c//=10
#print(b)
print(s)
print("Final step is add the reversed and new original number")
print("And that output is 👇")
second = first + s
print("Your Magic Number ➡️ ",second)
print("Want to try again ?")
print("Below AGAIN Button is present. Press and Feel the Magic..")