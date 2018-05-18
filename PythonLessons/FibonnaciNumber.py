# This is Naive algorithm for calculating nth term of Fibonnaci Sequence
# This is the big-O notation formula, T(n) = 3 + T (n-1) + T(n-2).
# Here we create the program to caclulate fibonnaci number
# First we assign two number in dynamic array or datastructer which is 0 and 1
# Then we add the number using recursive function

def fibRecursive(number):
    
    if number <= 1:
 
        return number
   
    return fibRecursive(number-1) + fibRecursive(number-2)
    
    
number = int(input("Input Max fib number"))
number = fibRecursive(number)
print (number)

# Here we have O(Log(n)) algorithm that fibbonnaci sequence
# we can use formula that derive from matrix
# If the number is EVEN then we can put k = n/2
# If n is odd, we can put k = ( n + 1 )/2

# we find the nth Fibbonacci number
# in with O(Log n) arithmatic operations
MAX =1000

# Create an array for allocating memory
fNumber = [0]* MAX

# Returns n'th fibonnaci number using table f[]
def fib(number) :
    # Base cases
    if(number == 0 ) :
        return 0
    if(number == 1 or number ==2):
        fNumber[number] = 1
        return (fNumber[number])

    # If fib(n) is already computed
    if (fNumber[number]):
        return fNumber[number]

    if(number & 1):
        k = (number + 1) //2
    else:
        k = number // 2

    # Applying aove formula [Note value number&1 is 1]
    # if number is odd, else 0.
    if((number & 1)) :
        fNumber[number] = (fib(k) * fib(k) + fib(k-1) * fib(k-1))
    else:
        fNumber[number] = (2*fib(k-1) + fib(k)) * fib(k)
    return fNumber[number]

# Driver code
number = 9
print(fib(number))

# This code is from Kikita Tiwari.
# The efficient of this program is O(n) 
# Efficient Algorithm
# using Dynmaic Programming
def FibEfCalculate(number):

    # Taking 1st two fibonacci numbers as 0 and 1
    FibArray = [0,1]

    # Here we append number on the list on the array
    while len(FibArray) < number + 1:
        FibArray.append(0)
    # here we return the number if it less than or equal to 1.
    if number <= 1:
        return number
    else:
        # Here we check for list value contain 0 or not
        # if it contain 0 then we call the recursive method to reduce the size of the number
        # This allow us to collect first number
        if FibArray[number - 1] == 0:
            FibArray[number - 1] = FibEfCalculate(number - 1)

        # Here we compare the value from list number
        # Simlar to above number we call the recursive method to reduce number in size
        # This allow us to collect second number
        if FibArray[number - 2] == 0:
            FibArray[number - 2] = FibEfCalculate(number - 2)
            
        # Then we add first and second number to appropriate index number
        FibArray[number] = FibArray[number - 2] + FibArray[number - 1]

    return FibArray[number]
    
# Driver code
print(FibEfCalculate(9))

#https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
