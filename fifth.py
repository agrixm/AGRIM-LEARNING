#classwork lab-1

a=float(input("Enter the first number: "))  
b=float(input("Enter the second number: "))
print("1. Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Exponentiation\n6.Modulus\n7.Floor Division")
c=int(input("Enter the operation you want to perform: "))
if c==1:
    print("The sum of",a,"and",b,"is",a+b)
elif c==2:
    print("The difference of",a,"and",b,"is",a-b)
elif c==3:
    print("The product of",a,"and",b,"is",a*b)
elif c==4:
    if b!=0:
        print("The Division of",a,"and",b,"is",a/b)
elif c==5:  
    print("The Exponentiation of",a,"and",b,"is",a**b)
elif c==6:
    print("The Modulus of",a,"and",b,"is",a%b)
elif c==7:
    print("The Floor Division of",a,"and",b,"is",a//b)

else:
    print("Invalid Input")


#Strings          
name="Agrim"
friend="Rohan"
other='Harsh'
print(name)
print('he said, "I want to eat an apple"')

chat= '''Hi Agrim 
how are you
what are you doing'''


for i in chat:
    print(i)


agrim="Agrim and he is best "
for character in agrim:
    print(character)


# slicing
a="Agrim"
print(a[0:-3])
print(a[0:len(a)-3])
print(a[-3:-1])

b="Harry"
print(b[-4:-2])