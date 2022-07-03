# 2. all_true — Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.

def all_true(iter):
  return all(iter)

print(all_true([True,True,True]))
print(all_true((True, False)))


# 3. one_true — Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

def one_true(iter):
  return any(iter)

print(one_true([True,True,True]))
print(one_true([False, False, False]))