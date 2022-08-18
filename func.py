"""#Functions :block of code which only will run when we call it
def trialfunction():
    print("Hello,World!")

trialfunction()    #function call
def demofuction(x):#parameter
    print(x+ " World")

demofuction("yello")#argument
#parameter both passes information,for a function its a veriable that is listed inside the parantheses in the function defined
#argument after calling the function what we pass through the argument its a argument
def testfunction(x,y):#multiparameter
    print(x+ " "+y)

testfunction("Blue","World")#multiargument if we give only one argument for two parameter typeError
#for loop is basically used to iterate sequence such as list,dictionary,tuple or string
numbers = [1,2,3,4,5,67,89,100]
for x in numbers:
    print(x)
x = "Fruits"

for a in x:
    print(a)
#break statement:It stops the loop befor everything gets covered
num = [10,20,30,40,50,60]
for x in num:
    print(x)
    if x== 40:
        break
#Continue statement:stop the loop and then start the next part
num = [1,2,3,4,5,6]
for x in num:
    print(x)
    if x== 4:
        continue
    print(x)
for x in range(100): #range function is basically something that returns sequence of numbers and it will start from zero by default
    print(x)
for y in range(40, 100):
    print(y)
#while loop :Python basically only has two loops in it which are the primitive loops while and the for
#while loop will let us execute a set of  statements while it is true
i = 1
while i<6:
    print(i)
    i += 1
i = 1
while i<6:
    print(i)
    if i==3:
        break
    i += 1"""
i = 1
while i<6:
    i += 1
    if i==3:
        continue#skips 3 and countinue loop
    print(i)


