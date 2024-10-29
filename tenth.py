#break 
for i in range(12):
    if(i==7):
       print("skip the loop")
       continue
    print("5 X",i,"=",5*i)

for i in [2,3,4,6,8,0]:
    if (i%2!=0):
        continue
    print(i)

for i in range(1,101,1):
    print(i ,end=" ")
    if(i==50):
        break
    else:
        print("Mississippi")
print("Thank you")

#functions
def mean(a,b):
    print((a*b)/(a+b))
    return mean
def isGreater(a,b):
    if a>b:
        print("a is greater than b")
    else:
        print("b is greater than a")
a=9
b=8
(mean(a,b))
(isGreater(a,b))
c=7
d=8
(mean(c,d))
(isGreater(c,d))


#default argument
def average(a=9,b=9):
    print("The average of two numbers is",(a+b)/2)


average(5)

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

name("Amy","agrim")

def name(fname,lname, mname ):
    print("Hello,", fname, lname, mname)

name( lname = "Wesker",mname = "Peter" ,fname="Chris")
def name(fname, mname):
    print("Hello,", fname, mname)

name("Peter")

def name(*hello):
    print("Hello,",hello[0],hello[1],hello[2])

name("James", "Buchanan", "Barnes", "Steve", "Rogers")


def name(**name):
    print("Hello,", name["fname"], name["mname"], name["lname"])

name( lname = "Barnes",mname = "Buchanan", fname = "James")


# return statement
def name(fname, mname, lname):
    return "Hello, " + fname +  mname + lname

print(name("James", "Buchanan"))

