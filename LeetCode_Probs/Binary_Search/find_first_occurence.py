# In a sorted array of numbers
# Find first occurence of a number

# With Normal Binary Search, when we find an occurence, we stop
# But here, we need to find the first occurence

# So if we find the occurence
# Then if that is the first occurence, then we won't find any more occurences @left
# Otherwise we can find more occurences @left

# Since it is sorted order, @left always decreasing

# 1, 1, 1, 1, 1, 2, 2, 3, 4
# m_p = 4
# Array to the left: 1, 1, 1, 1
# Again if midpoint is >= that number, we go to the left
# If mid_point is < number, we know it is on the right
# Keep a track of last found occurence of K
# This way whenever it quits, we know what to return

# M_P = 2 -> 1
# Array to the left: 1, 1
# M_P = 0
# Array to the left doesn't exist, so last found occurence of K

# 0, 0, 0, 1, 1, 2, 2, 3, 4
# M_P = 4 -> 1
# Array to the Left: 0, 0, 0, 1
# M_P = 2 -> 0
# Since M_P < Number, go to the right
# Array to the Right: 1
# M_P = 0 -> 1
# Array to the left doesn't exist, so last found occurence of K

# 0, 0, 1, 1, 1, 2, 2, 3, 4
# M_P = 4 -> 1
# Array to the Left: 0, 0, 1, 1
# M_P = 2 -> 1
# Since M_P >= Number, go to left
# Array to the Left: 0, 0
# M_P = 0 -> 0
# Array to the right: 0
# Again < K, but Array to right doesn't exist, so return last found occurence of K


def find_first_occurence(arr, k):
    l_p = 0
    r_p = len(arr) - 1
    k_found = -1 # Update whenever a K is found

    while l_p <= r_p:
        m_p = (l_p + r_p)//2
        m_p_val = arr[m_p]

        if k==m_p_val:
            k_found = m_p
        
        if m_p_val >= k:
            # Go to the left
            r_p = m_p - 1

        else: # Go to the right
            l_p = m_p + 1

    return k_found

print(find_first_occurence([0, 0, 1, 1, 1, 2, 2, 3, 4], 1))
print(find_first_occurence([0, 0, 0, 1, 1, 2, 2, 3, 4], 1))
print(find_first_occurence([0, 0, 0, 1, 1, 2, 2, 3, 4], 0))
print(find_first_occurence([1, 1, 1, 1, 1, 2, 2, 3, 4], 1))
print(find_first_occurence([1, 2, 3, 4, 5, 6, 7, 7, 8], 7))
print(find_first_occurence([1, 2, 3, 4, 5, 6, 7, 7, 8], 0))
print(find_first_occurence([1, 2, 3, 4, 5, 6, 7, 7, 8], 2))
print(find_first_occurence(["a", "b", "b", "c", "c", "d", "e", "e", "f"], "c"))
print(find_first_occurence(["a", "b", "b", "c", "c", "d", "e", "e", "f"], "z"))