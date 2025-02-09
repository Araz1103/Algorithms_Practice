"""
Slicing with arr[start:end:step]
If step is negative, starts from backwards
"""

arr = [0, 1, 2, 3, 4, 5]
print(arr[::-1])
# Output: [5, 4, 3, 2, 1, 0]

arr = [0, 1, 2, 3, 4, 5]
print(arr[::-2])
# Output: [5, 3, 1]

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(arr[::-3])
# Output: [8, 5, 2]

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(arr[-3:-8:-3])
# Output: [6, 3]
# Starts from -3 (6) till -8 (1)
# In reverse order, 3 steps
# So, after 6, 3 steps
# 5, 4, '3'
# Thus returns [6, 3]

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(arr[-3:-8])
# Output: []
# Starts from -3 (6) till -8 (1)
# Since steps are positive, needs to go in forward order
# But based on the slice nothing in forward
# So just returns []

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(arr[-8:-3:2])
# Output: [1, 3, 5]
# Starts from -8 (1) till -3 (6)
# Since steps are positive, needs to go in forward order
# So after 1, 2 steps
# 2, '3'
# After 3, 2 steps
# 4, '5'
# So returns [1, 3, 5]

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(arr[-8:-3])
# Output: [1, 2, 3, 4, 5]
# Starts from -8 (1) till -3 (6)
# Since steps are positive, needs to go in forward order
# 6 is not inclusive, so stops till 5
# So returns [1, 2, 3, 4, 5]

