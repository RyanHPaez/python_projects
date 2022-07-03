# Write a Python function called max_num()to find the Max of three numbers.

def max_num(a,b,c):
  return max([a,b,c])

print(max_num(1,2,3))
print(max_num(300,200,100))
print(max_num(2000,3000,1000))

# min_num

def min_num(a,b,c):
  return min([a,b,c])

print(min_num(1,2,3))
print(min_num(300,200,100))
print(min_num(2000,3000,1000))

#average number

a_list = [100, 200, 300]

sum = sum(a_list)
# Get total sum of `a_list`

length = len(a_list)
# Get the length of `a_list`

average = sum/length
# Calculate average


print(average)