# This is how an infinite loop works
'''
while 1:
    print ("You cannot stop this")
    break
'''

# This loop work until given number
'''count = 0
while count < 10:
    print("Hello, I am a while and count is", count)
    count += 1
'''

# The following scripte calculates the sum
# of the numbers from 1 to 100

n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print ("Sum of 1 until %d: %d" % (n, sum))
