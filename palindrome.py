#  program should take in a string and return True if the string is a palindrome and False if not
#  A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.
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
# ------------------------------------------------------------


def solution(inputString):
    count=[0]*256
    for i in inputString:
        count[ord(i)]+=1
    odd=0
    for i in range(0,256):
        if(count[i]&1):
            #print(count[i],chr(i))
            odd+=1
           # print(odd)
        if(odd>1):
            return False
    return True
inputString = "aabb"
print(solution(inputString))