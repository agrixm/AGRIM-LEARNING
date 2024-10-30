#lists

l=[1,2,3,4,5,6,7,8,9,10]
print(type(l))
print(l[0])




#string-indexing
a="Hello"
print(a[0])


# list can have multiple data types

l=[1,True,"Hello",3.5]  
print(l)

l=["agrim","amy","peter","chris","jill","leon","claire","jake","sherry","ada"]
print(l[-5])
print(len(l))
if "jill" in l:
    print("Yes")
else:    
    print("No")
print(l[0:5])
print(l[-6:-5])
print(l[:5])


animals = ["cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow"]
print(animals[3:7])	
print(animals[-7:-2])	



#lIST mETHODS
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [1,2,1,3,4,5]

num.insert(2,3)
print(num)

colors = ["red","blue"]
num=[1,2,3]
colors.extend(num)  
print(colors)

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

num = (1,2,3,4)
temp=list(num)
temp.insert(1,"Green")
num=tuple(temp)
print(num)