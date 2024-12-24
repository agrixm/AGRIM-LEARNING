# print("""Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the trav'ller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often thro' my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the trav'ller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star.""" )

# a=6
# a-=9
# print(a)


# d=5<6
# print(d)

# e=True and False
# print(e)


# print(not(True))

# a=None 
# print(type(a))

# a=1
# b=float(a)
# print(type(b))
# print(b)

# a=int(input("Enter the Number 1"))
# b=int(input("Enter the Number 2"))

# print("Remainder is",a%b)


# a="1"
# print(type(a))

# a=input("Enter the value of A :")
# b=input("Enter the value of B :")

# print(a>b)

# a=int(input("Enter the value of A :"))

# b=int(input("Enter the value of B :"))

# print((a+b)/2)



# a=int(input("Enter the value of A :"))

# print("Sqaure is",a*a)


# a="Agrim is a good boy"
# # print(len(a))
# b=a[-4:-1]
# print(b)

# a="HARRY"
# b=a[-4:-1]
# print(b)

# a="abcdefghijklmnopqrstuvwxyz"
# print(a[1:9:4])

# a="agrim are are "
# # print(len(a))
# # print(a.endswith("im"))
# # print(a.startswith("hiu"))
# # print(a.capitalize())
# # print(a.count("a"))
# # print(a.find("r"))
# print(a.replace("are","latika"))


# a="""jai ho 
# my nname is"""
# print(a)

# a="agrim is a good boy but harry is a boy\\"
# print(a)

# a=input("enter the name")
# print(f"{a} is good boy")

# a=j6
# print(type(a))

# a="my name is agrim  and  im  a good boy"
# print(a.replace("  "," "))
# print(a)

# a=["agrim",1,2.3,True]
# a[1]=False
# print(a[0:2])

# a=(0,1,2,4,1,3,1,5,7,9,"Agrim")
# b=len(a)
# print(b)


# a=[]
# f1=input("Enter fruits name ")
# a.append(f1)
# print(a)

# a=(34,"Harry")
# a[2]="larry"

# l=(34,45,65,21,0,0,0,0)
# b=l.count(0)
# print(b)

# marks = {
#     "Agrim":100,
#     "shubam":300
# }
# # print(marks.keys())
# # print(marks.values())
# marks.pop("Agrim","shubam")

# print(marks)

# s={1,2,3,4,5}
# s2={2,3,4}
# print(s.difference(s2))


# Words = {
#     "Naam" : "name",
#     "Kursi": "Chair"

# }
# a=input("Enter the Word")
# print(Words[a])

# n=input("Enter number :")
# s=set()
# s.add(int(n))
# n=input("Enter number :")
# s.add(int(n))
# n=input("Enter number :")
# s.add(int(n))
# n=input("Enter number :")
# s.add(int(n))
# n=input("Enter number :")
# s.add(int(n))

# print(s)

# s=set()
# s.add(18)
# s.add("18")
# print(s)

# s={1,2,3}
# print(type(s))

# e={}
# Name = input("enter the name")
# Language = input("Enter language")

# e.update({Name: Language})
# Name = input("enter the name")
# Language = input("Enter language")

# e.update({Name: Language})
# Name = input("enter the name")
# Language = input("Enter language")

# e.update({Name: Language})

# print(e)


# a=int(input("Enter Age :"))
# if(a>18):
#     print("adult")
# else:
#     print("child")

# a1=int(input("Enter The Number"))
# a2=int(input("Enter The Number"))
# a3=int(input("Enter The Number"))
# a4=int(input("Enter The Number"))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("A1 is greatest")
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("A2 is greatest")
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("A3 is greatest")
# else:
#     print("A4 is greatest")

# for i in range(100):
#     if(i==34):
#         continue
#     print(i)

# n=int(input("enter the number"))

# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")


def goodday(name):
    print("Good day" + name)


goodday(" Agrim")