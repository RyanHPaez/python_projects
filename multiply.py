# Write a Python function called mult_list()  to multiply all the numbers in a list.

def mult_list(lst):
  #if empty list, return 0
  if len(lst) == 0:
    return 0
  #product starts with first element of list
  prod = lst[0]

  #go through list elements and multiply them together
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
    
print(mult_list([1,2,3]))
print(mult_list([3,2,1]))
print(mult_list([9]))
print(mult_list([3,3,2]))