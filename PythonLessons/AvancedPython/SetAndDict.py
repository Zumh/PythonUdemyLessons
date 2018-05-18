# Create a set
items = {"arrow", "spear", "arrow", "arrow", "rock"}

#print set
print (items)
print (len(items))

if "rock" in items:
    print("Cloak not found")
    

#Create an empty set

items = set()

#add
items.add("cat")
items.add("dog")
items.add("fish")
print(items)

numbers1 = {1,3,5,7}
numbers2 = {1,3}

if numbers2.issubset(numbers1):
    print("Is a subset")

if numbers1.issuperset (numbers2):
    print ("Is a Superset")

print ( numbers1.intersection(numbers2) )

 

    
