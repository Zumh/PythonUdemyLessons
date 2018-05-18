value = "cat picture is cat picture"

#Find first index of this string
i = value.find("picture")
print(i)

#Find first index (of this string) after previous index
b = value.find("picture", i +1)
print (b)

vlaue = "realph waldo emerson"
i = value.find("python")

if i != -1:
    #not found
    print ("String not found")
else:
    print ("String not found")

value = "cat picture is cat picture"
#start with this value
location = -1

#Loop while true
while True:
    #advance location by -1
    location = value.find ("picture", location + 1)

    #break if not found
    if location == -1: break

    #display the location
    print (location)
    
# Using the reverse finding string 
value = "cat picture is cat picture"

#get the rightost index of the string
i = value.rfind("picture")
print(i)


#get the rightmost index within this range of characters

b = value.rfind ("picture", 0, i - 1)
print (b)

# Using the reverse finding string in the while Loop
vlaue = "cat picture is cat picture"

#start with length of string
i = len(value)

while True:
     #find rightmost string in this range
     i = value.rfind ("picture", 0, i)

     #check for not found
     if i == -1: break;
     print (i)
     
    
