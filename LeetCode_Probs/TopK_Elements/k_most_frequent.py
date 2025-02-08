"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# Approach
# First make a Hashmap of all the items with their counts
# Gets us all unique items and their counts

# Now we need to return the top most frequent out of them based on k
# If we sort them based on the counts, and then return that can work
# So add them in a list and use sort by key, where we choose the value (frequency)
# This will make the overall complexity to O(n log n)

# But if we don't want to sort once we have the frequencies
# Let's say K is 1
# Then we iterate through frequencies and based on a max count, always get the max count
# That is just O(n), another iteration

# If K is 2
# Then we have 2 max counts
# If it's > 1,  update that, less than 1, don't update that
# Basically in 1 iteration comparing K times to keep the K most frequent

# This can make overall complexity dependent on K
# So O(n*k)
# Worst case if k = n, then it's O(n^2)
# But in that case, if we know k == n, we can just directly return all items
# For k = n - 1, we can return all but the least one, so we have to find the least one 

# Need to use Heaps for O(N*LogK)

def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    frequency_dict = {}
    for elem in nums:
        if elem not in frequency_dict:
            frequency_dict[elem] = 1
        else:
            frequency_dict[elem] += 1

    # Naive way
    sorted_count = [[elem, cnt] for elem, cnt in frequency_dict.items()]
    sorted_count.sort(key=lambda x: x[1], reverse=True)

    # Return top k elements
    ans = [elem for elem, cnt in sorted_count[:k]]
    return ans

nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))

nums = [1]
k = 1
print(topKFrequent(nums, k))

 