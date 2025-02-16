"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Binary Search until we find a bad version
        # Keep track of last bad version found
        # Go the the left until you can't more
        # If not a bad version, this means search on right to find one
        left_idx = 1
        right_idx = n
        last_found = -1

        while left_idx <= right_idx:
            mp_idx = int(left_idx + (right_idx - left_idx)/2)

            if isBadVersion(mp_idx):
                last_found = mp_idx
                # Check if any more on the left
                right_idx = mp_idx - 1
            else: # If not check on the right if there is any bad version
                left_idx = mp_idx + 1

        return last_found

        