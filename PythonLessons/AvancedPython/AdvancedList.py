# Working with advanced lists

nums = [1,2,3,4,7,8,9]
#    0,1,2,3,4,5 There are the index

print (nums.index(4))
del nums[2]
print (nums)

nums.insert(1, 10)
print (nums)
nums.insert(0, [33,44,22])
print(nums)
#List of numbers that square from x to range 10 and can be squre 
nums = [x**2 for x in range(10) if x%2 == 0]
print (nums)


