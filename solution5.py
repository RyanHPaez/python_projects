# Write code for algorithm 5 below
def is_palindrome(str):
  if len(str) == 1 or len(str) == 0:
    return True
  else:
    return (str[0] == str[-1]) and is_palindrome(str[1:-1])

print("is 'apple' a palindrome?")
print(is_palindrome('apple'))
print("is 'tacocat' a palindrome?")
print(is_palindrome('tacocat'))