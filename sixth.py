
print("Enter the first number: ")
a=input()
print("Number is: ", a)
print("Enter the second number: ")
b=input()
print("Number is: ", b)
print("1. Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Exponentiation\n6.Modulus\n7.Floor Division")
print("Enter the operation you want to perform: ")
c=input()
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
    
