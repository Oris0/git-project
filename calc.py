ans = input("what will you want to do S or A: ")




x = float( input("insert first num : "))
y =  float(input("insert second num: "))

if ans == "S":
   result = x-y
   print (f"{result}")
elif ans== "a":
   result = x * y
   print (f"{result}")

else: 
    print ("useyourhead")

