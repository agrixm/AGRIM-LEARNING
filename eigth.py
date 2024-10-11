import time
timestamp = time.strftime('%H:%M:%S')
print("The time is",timestamp)
if(timestamp<"12:00:00"):
    print("Good Morning")

elif(timestamp>"12:00:00" and timestamp<"17:00:00"):
    print("Good Afternoon") 

elif(timestamp>"17:00:00"):
    print("Good Evening")




