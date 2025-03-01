"""
Given an array of values, design a Data Structure that can 
query the sum of a subarray of values
"""

class PrefixSum:
    def __init__(self, arr):
        # if not arr:
        #     self.prefix_sums = []
        # else:
        #     self.prefix_sums = [arr[0]]
        
        #     for idx in range(1, len(arr)):
        #         prefix_sum = self.prefix_sums[idx-1] + arr[idx]
        #         self.prefix_sums.append(prefix_sum)
        total = 0
        self.prefix_sums = []
        for num in arr:
            total+=num
            self.prefix_sums.append(total)

        self.postfix_sums = [0 for i in range(len(arr))]
        total = 0
        for idx in range(len(arr)-1, -1, -1):
            total += arr[idx]
            self.postfix_sums[idx] = total


    def query_sum(self, l, r):
        """
        Returns the sum of elements of an array between l and r
        Use the Prefix Sums we calculate to get this in O(1)
        We know Pre-fix sum till r
        We know Pre-Fix sum till l-1
        So sum between l and r is PS(r) - PS(l-1)
        So if l > 0, then above
        If l is 0, then we can just return PS(r)
        """
        if l > 0:
            return self.prefix_sums[r] - self.prefix_sums[l-1]
        else:
            return self.prefix_sums[r]
        
ps = PrefixSum([1, 3, -4, 0, 2, 14, 3, -10, 11, 4])
print(ps.prefix_sums)
print(ps.query_sum(2, 5))
print(ps.query_sum(0, 5))
print(ps.query_sum(1, 6))
print(ps.query_sum(4, 9))
print(ps.postfix_sums)
