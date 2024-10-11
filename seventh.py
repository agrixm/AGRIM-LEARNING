#STRINGS
a= '''अपने पसंदीदा गैजेट को अनलॉक करने और चुनने के लिए ग्लू नोवा इवेंट में 
भाग लें। मि वैगर को बरमूडा को साफ करने और इस प्रक्रिया में अपने दुश्मनों को खत्म करने
में मदद करें! ... लीला, एक ग्लू आर्टिस्ट,
ग्लू से अपनी प्रेरणा लेती है.'''
print("hello",a)

a="agrim"
print(a[1])
print(a[2]) 
print(a[3])         
print(a[4])
print(a[0:5])
print("Length of string is")
for character in a:
    print(character)

a="agrim, is a good"
print(a[0:9])
print("HOW MANY LETTERS",len(a))
b="Apple" 
print(b[0:-1])  #-----> #print(b[0:len(b)-1])
print(b[-1:-1])

c="agrim"
print(c[-4:-2])



d="aJriM"
print(d.upper())    

e="AGrim"
print(e.lower())

f="###agrim:::::****"
print(f.strip("#:*"))  #strip() removes the leading and trailing characters


g="intro tO pYthon"
print(g.capitalize())  #capitalize() makes the first letter of the string capital

h="agrim is a good boy"
print(h.center(40))
print(len(h.center(40)))
print(len(h))

a="agrim is a "
print(a.find("good"))  #find() returns the index of the first occurence of the substring
print(a.isalnum())

z="agrim is a 6"

print(z.isalnum())

i="agrim is A"
print(i.islower())

y="Agrim Is A good Boy"
print(y.istitle())

y="agrim is a good booy"
print(y.title())
