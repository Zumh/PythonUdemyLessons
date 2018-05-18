# This is the program that use find to loop the through the sentence for finding a word

value = "cat picture is cat picture"

#Find first index of this string
position = value.find("picture")
print(position)

#Find first index ( of this string) after previous index
secondPosition = value.find("picture", position + 1)
print(secondPosition)

# HERE WE FIND  WORD USING TRAVERSING THE LOOP IN LINEAR APPROACH.
value = "ralph waldo emerson"
position = value.find("python")
if position != 1:
    #not found
    print ("String found")
else:
    print ("String not found")

value = "cat picture is cat picture"
#start with this value
location = -1
#Loop while true
while True:
    #advance location by -1
    location = value.find("picture", location + 1)

    #break if not found
    if location == -1: break

    #display the location
    print(location)



# HERE WE USE REVERSE LOOP TO FIND A WORD IN A SENTENCE
value = "cat picture is cat picture"

#get the rightmost index of the string
position = value.rfind("picture")
print(position)

#get the rightmost index within range of chracters
secondPosition = value.rfind("picture", 0, position -1)
print(secondPosition)

#start with length of string
position = len(value)

while True:
    #find rightmost string in this range
    position = value.rfind("picture", 0, position)

    #check for not found
    if position == -1:break
    print(position)
    



    

