# Calculating miles per gallon
print ("This program calculate mpg")

# Ask input from the user
milesDriven = input("Enter miles driven: ")

# convert test entered to a float point number
milesDriven = float (milesDriven)

#Get gallons used from the user
gallonsUsed = input ("Enter gallons used: ")

#Convert text entered to a float point number
gallonsUsed = float (gallonsUsed)

#Calculate and print the answer
mpg = milesDriven / gallonsUsed
print ("Miles per gallon: ", mpg)
