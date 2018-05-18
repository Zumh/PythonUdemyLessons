# Fibonnaci numbers module

def fib(n): #This will write Fibonnaci series upto n
    a, b = 0, 1
    while b < n:
        print (b, end='')
        a,b = b, a+b
        print()

def fib2(n): # This will retun Fibonnaci series up to n
    result = []
    a,b = 0, 1
    while b < n:
        result.append(b)
        a,b = b, a+b

    return result
    
