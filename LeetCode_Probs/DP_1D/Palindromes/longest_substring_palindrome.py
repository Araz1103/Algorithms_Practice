def check_palindrome(s):
    # Using 2 pointers
    # Check in O(N)
    l = 0
    r = len(s)-1
    while l < r:
        if s[l]!=s[r]:
            return False
        l+=1
        r-=1
    return True

# print(check_palindrome("araz"))
# print(check_palindrome("a"))
# print(check_palindrome("arazara"))
# print(check_palindrome("as"))
# print(check_palindrome("aa"))
# print(check_palindrome("arazzara"))

# BRUTE FORCE
def get_longest_palindrome(s):
    # For a string s, we want the length of the longest palindrome within s
    # brute force soln
    # Get all sub-strings, and check for each of them if it is a palindrome
    # Getting all sub-strings is O(N^2, 2 for loops
    # Checking if a sub-string is a palindrome is O(N)
    # So worst case: O(N^3) for Brute Force!
    max_len = 1 #default
    for idx in range(len(s)):
        sub_string = ""
        for jdx in range(idx, len(s)):
            sub_string+=s[jdx]
            if check_palindrome(sub_string):
                print(f"Found! :{sub_string}")
                max_len = max(max_len, len(sub_string))

    return max_len

print(get_longest_palindrome("araz"))
print(get_longest_palindrome("abaab"))

# Optimised
# Normally to check for palindromes we start at the edges with L and R, and keep checking if it is a palindrome or not
# But if we did the opposite
# Start at the middle, and then keep expanding outwards to see if palindrome or not, until not a palindrome
# or we cannot expand (out of bounds)
# With this, we can check while doing a pass on the string
# So in the single pass, we can keep expanding assuming each character is the middle palindrome character, 
# till not a palindrome or goes out of bounds, cannot expand
# So time complexity is N^2 (single pass is N, and at each character expanding is N)

# Now there are 2 cases to handle here
# If the palindrome is odd or even length
# Odd lenght is straightforward
# Assuming each char is middle char of palindrome, we can check L and R of that, and see if valid palindrome or not
# Keep updating max len found (or sub-string palindrome too)

# If even length, rather than just take a single char as middle
# We do a pass assuming 2 chars together as middle chars
# If they are equal, we can then expand checking if palindrome
# If they are not equal, then stop there itself, since cannot be a palindrome

# So approach is to do 2 passes, one for odd length palindromes and one for even length palindromes
# Time for each of them will be N^2
# Total Time Complexity: 2*N^2 = O(N^2)
# Space Complexity is O(1), since we check in place

def get_longest_palindrome(s):
    
    max_len = 1 #default
    max_palindrome = ""
    # First Odd Length Pass
    # Assume each char as middle palindrome char
    for idx in range(len(s)):
        L, R = idx, idx
        while L >= 0 and R < len(s):
            if s[L]==s[R]:
                # Valid Palindrome
                # Update Max Len Found
                if (R-L+1) >= max_len:
                    max_len = R-L+1
                    max_palindrome = s[L:R+1]
                #max_len = max(max_len, R-L+1)
                L-=1 #Expand L pointer
                R+=1 #Expand R Pointer
            else:
                break #No need to expand further!

    # Now Even Length Pass
    # Assume 2 chars as middle palindrome char
    # Now we check idx till 1 before the final char
    for idx in range(len(s)-1):
        L, R = idx, idx+1
        while L >= 0 and R < len(s):
            if s[L]==s[R]:
                # Valid Palindrome
                # Update Max Len Found
                if (R-L+1) >= max_len:
                    max_len = R-L+1
                    max_palindrome = s[L:R+1]
                #max_len = max(max_len, R-L+1)
                L-=1 #Expand L pointer
                R+=1 #Expand R Pointer
            else:
                break #No need to expand further!
    return max_len, max_palindrome

# In 1 iteration, calculate both even and odd lengths
# No change in Time complexity, but saves another pass
# Also can write the duplicate code in a helper function if needed!
# Also can add the s[L]==s[R] check in the while loop condition itself
# But this is more readable probably :P
def get_longest_palindrome(s):
    
    max_len = 1 #default
    max_palindrome = ""
    # First Odd Length Pass
    # Assume each char as middle palindrome char
    for idx in range(len(s)):
        L, R = idx, idx
        while L >= 0 and R < len(s):
            if s[L]==s[R]:
                # Valid Palindrome
                # Update Max Len Found
                if (R-L+1) >= max_len:
                    max_len = R-L+1
                    max_palindrome = s[L:R+1]
                #max_len = max(max_len, R-L+1)
                L-=1 #Expand L pointer
                R+=1 #Expand R Pointer
            else:
                break #No need to expand further!

        # Now Even Length Pass
        # Assume 2 chars as middle palindrome char
        # Now we check idx till 1 before the final char
        L, R = idx, idx+1
        while L >= 0 and R < len(s):
            if s[L]==s[R]:
                # Valid Palindrome
                # Update Max Len Found
                if (R-L+1) >= max_len:
                    max_len = R-L+1
                    max_palindrome = s[L:R+1]
                #max_len = max(max_len, R-L+1)
                L-=1 #Expand L pointer
                R+=1 #Expand R Pointer
            else:
                break #No need to expand further!
    return max_len, max_palindrome

print(get_longest_palindrome("araz"))
print(get_longest_palindrome("abaab"))
print(get_longest_palindrome("abaabaa"))
