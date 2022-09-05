# Given an array a, your task is to apply the following mutation to it:

# Array a mutates into a new array b of the same length
# For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it is considered to be 0
# For example, b[0] equals 0 + a[0] + a[1]
# Example

# For a = [4, 0, 1, -2, 3], the output should be solution(a) = [4, 5, -1, 2, 1].

# Explanation:

# b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
# b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
# b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
# b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
# b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1
# So, the mutated answer array is [4, 5, -1, 2, 1].


# -----------------------------------------------------------------------------
# You are given a string s. Your task is to count the number of ways of splitting s into three non-empty parts a, b and c (s = a + b + c) in such a way that a + b, b + c and c + a are all different strings.

# NOTE: + refers to string concatenation.

# Example

# For s = "xzxzx", the output should be solution(s) = 5.

# Consider all the ways to split s into three non-empty parts:

# If a = "x", b = "z" and c = "xzx", then all a + b = "xz", b + c = "zxzx" and c + a = xzxx are different.
# If a = "x", b = "zx" and c = "zx", then all a + b = "xzx", b + c = "zxzx" and c + a = zxx are different.
# If a = "x", b = "zxz" and c = "x", then all a + b = "xzxz", b + c = "zxzx" and c + a = xx are different.
# If a = "xz", b = "x" and c = "zx", then a + b = b + c = "xzx". Hence, this split is not counted.
# If a = "xz", b = "xz" and c = "x", then all a + b = "xzxz", b + c = "xzx" and c + a = xxz are different.
# If a = "xzx", b = "z" and c = "x", then all a + b = "xzxz", b + c = "zx" and c + a = xxzx are different.
# Since there are five valid ways to split s, the answer is 5.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string to split.

# Guaranteed constraints:
# 3 ≤ s.length ≤ 100.

# [output] integer

# The number of ways to split the given string.
def solution(s):
    ans = 0
    for i in range(len(s) - 2):
        for j in range(i+1,len(s) - 1):
            a = s[:i+1]
            b = s[i+1:j+1]
            c = s[j+1:]
            if a+b != b+c and a+b != c+a and b+c != c+a:
                ans = ans + 1
    return ans

# -------------------------------------------------------------------------------------------------
# Given a matrix of integers, we'd like to consider the sum of the elements within the area of a 45° rotated rectangle. More formally, the area is bounded by two diagonals parallel to the main diagonal and two diagonals parallel to the secondary diagonal. The dimensions of the rotated rectangle are defined by the number of elements along the borders of the rectangle.

# dimensions

# Given integers a and b representing the dimensions of the rotated rectangle, and matrix (a matrix of integers), your task is to find the greatest sum of integers contained within an a x b rotated rectangle.

# Note: The order of the dimensions is not important - consider all a x b and b x a rectangles.

# Example

# For

# matrix = [[1, 2, 3, 4, 0],
#           [5, 6, 7, 8, 1],
#           [3, 2, 4, 1, 4],
#           [4, 3, 5, 1, 6]]
# a = 2, and b = 3, the output should be solution(matrix, a, b) = 36.

# example 1

# For

# matrix = [[-2, 3, 5, -1],
#           [4, 3, -10, 10]]
# a = 1, and b = 1, the output should be solution(matrix, a, b) = 10.

# example 2

# The rotated rectangle with dimensions 1x1 is just one element, so the answer is the maximal element in matrix.

# For

# matrix = [[-2, 3],
#           [4, 3]]
# a = 1, and b = 2, the output should be solution(matrix, a, b) = 7.

# example 3

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] array.array.integer matrix

# A matrix of integers.

# Guaranteed constraints:
# 1 ≤ matrix.length, matrix[i].length ≤ 50,
# -103 ≤ matrix[i][j] ≤ 103.

# [input] integer a

# The first rotated rectangle dimension.

# Guaranteed constraints:
# 1 ≤ a ≤ 25.

# [input] integer b

# The second rotated rectangle dimension.
# It's guaranteed that at least one rotated rectangle will fit in the given matrix.

# Guaranteed constraints:
# a ≤ b ≤ 25.

# [output] integer

# The maximal sum of elements of a rotated rectangle with dimensions a and b.
# swift code
# func findMaxSum(matrix: [[Int]], a: Int, b: Int) -> Int {
# func inMatrix(_ point: (Int, Int)) -> Bool {
#     point.0 >= 0 && point.0 < matrix.count && point.1 >= 0 && point.1 < matrix.first!.count
# }

# func calculateMaxSumFor(a: Int, b: Int) -> Int {
#     var maxSum = Int.min

#     for i in 0..<matrix.count {
#         for j in 0..<matrix.first!.count {
#             var sum = 0

#             let left = (i+a, j-a)
#             let right = (i+b, j+b)
#             let bottom = (i+a+b, j-a+b)

#             guard inMatrix(left), inMatrix(right), inMatrix(bottom) else { continue }
            
#             var leftOffset = 0
#             var rightOffset = 0
            
#             var hasReachedLeft = false
#             var hasReachedRight = false
            
#             for m in i...i+a+b {
#                 for n in j-leftOffset...j+rightOffset {
#                     sum += matrix[m][n]
#                 }
                
#                 if leftOffset == a {
#                     hasReachedLeft = true
#                 }
                
#                 if rightOffset == b {
#                     hasReachedRight = true
#                 }
                
#                 if hasReachedLeft {
#                     leftOffset -= 1
#                 } else {
#                     leftOffset += 1
#                 }
                
#                 if hasReachedRight {
#                     rightOffset -= 1
#                 } else {
#                     rightOffset += 1
#                 }
#             }
            
#             maxSum = max(maxSum, sum)
#         }
#     }
    
#     return maxSum
# }

# return max(calculateMaxSumFor(a: a-1, b: b-1), calculateMaxSumFor(a: b-1, b: a-1))

# def rectangleRotation(a, b)
#     aHalfBisect = (a/Math.sqrt(2))/2
#     bHalfBisect = (b/Math.sqrt(2))/2
#     rect1 = [aHalfBisect.floor*2 + 1, bHalfBisect.floor*2 + 1]
#     rect2 = []
    
#     if aHalfBisect - aHalfBisect.floor < 0.5 
#         rect2[0] = rect1[0] - 1
#     else 
#         rect2[0] = rect1[0] + 1
#     end 
    
    
#     if bHalfBisect - bHalfBisect.floor < 0.5 
#         rect2[1] = rect1[1] - 1
#     else 
#         rect2[1] = rect1[1] + 1
#     end 
    
#     rect1.inject(:*) + rect2.inject(:*)
# end

# -------------------------------------------------------------------------------------------------------------
# An integer n is called a full square, if there exists some integer s, such that n = s * s. Examples of full squares are 0, 1, 4, 9, 16, etc.

# Given an array of distinct integers numbers, your task is to find the number of pairs of indices (i, j) such that i ≤ j and the sum numbers[i] + numbers[j] is a full square.

# Example

# For numbers = [-1, 18, 3, 1, 5], the output should be solution(numbers) = 4.

# There is one pair of indices where the corresponding elements sum up to 0:

# (0, 3): numbers[0] + numbers[3] = -1 + 1 = 0.
# There are two pairs of indices where the corresponding elements sum up to 4:

# (0, 4): numbers[0] + numbers[4] = -1 + 5 = 4;
# (2, 3): numbers[2] + numbers[3] = 3 + 1 = 4.
# There is one pair of indices where the corresponding elements sum up to 36:

# (1, 1): numbers[1] + numbers[1] = 18 + 18 = 36;
# In total, there are 1 + 2 + 1 = 4 pairs summing up to full squares.

# For numbers = [2], the output should be solution(numbers) = 1.

# The only pair of indices is (0, 0) and the sum of corresponding elements is equal to numbers[0] + numbers[0] = 2 + 2 = 4, which is a full square. So the answer is 1.
# For numbers = [-2, -1, 0, 1, 2], the output should be solution(numbers) = 6.

# There are three pairs of indices where the corresponding elements sum up to 0: (0, 4), (1, 3), and (2, 2).
# There are two pairs of indices where the corresponding elements sum up to 1: (1, 4) and (2, 3).
# There is one pair of indices where the corresponding elements sum up to 4: (4, 4).
# In total, there are 3 + 2 + 1 = 6 pairs summing up to full squares.
# Input/Output

# [execution time limit] 8 seconds (py3)

# [input] array.integer numbers

# An array of distinct integers.

# Guaranteed constraints:
# 1 ≤ numbers.length ≤ 4 · 104,
# -2 · 104 ≤ numbers[i] ≤ 2 · 104.

# [output] integer

# The number of pairs of indices (i, j) such that i ≤ j and the sum of the corresponding elements is equal to some full square.


# Given an array of integers a, your task is to calculate the digits that occur the most number of times in the array. Return the array of these digits in ascending order.