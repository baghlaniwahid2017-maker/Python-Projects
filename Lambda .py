
# Lambda filter  for even number
nums = [1,2,3,4,5,6,7,8,9,10]
even =list(filter(lambda x: x % 2 == 0, nums))
print(even)

# Lambda filter for odd number
nums = [1,2,3,4,5,6,7,8,9,10]
odd =list(filter(lambda x: x % 2 != 0, nums))
print(odd)


# Reduce
from functools import reduce

nums = [1,2,3,4,5]

result = reduce(lambda x,y: x * y, nums)
print(result)