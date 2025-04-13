from typing import List

# Approach I: Cache as a grid
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # @each element, choice to add it to current sum or subtract it
        # @end, need to check if we reached target, and get the ways

        def check_get_target(num_index, current_sum, cache):
            
            # Now all elements taken
            if num_index >= len(nums):
                # Check @target or not
                if current_sum==target:
                    return 1 #Found 1 way
                else:
                    return 0 # Reached @end and not at target
            
            # Check from cache
            if cache[num_index][current_sum]!=-1:
                return cache[num_index][current_sum]

            # Can add to current sum or subtract from it

            # Add to it
            num_ways_add = check_get_target(num_index + 1, current_sum + nums[num_index], cache)

            # Subtract from it
            num_ways_subtract = check_get_target(num_index + 1, current_sum - nums[num_index], cache)

            # Return total ways to reach target from here
            cache[num_index][current_sum] = num_ways_add + num_ways_subtract
            return cache[num_index][current_sum]

        # Initialise Cache
        # Using a hashmap as a cache can be easier
        # the current sum can range from sum of all negative elements to sum of all positive elements
        total_sum_range = len(range(sum([-1*num for num in nums]), sum(nums)+1))
        cache = [[-1]*(total_sum_range) for _ in range(len(nums))]
        return check_get_target(0, 0, cache)
    
# Approach II: Cache as a Hashmap
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        # @each element, choice to add it to current sum or subtract it
        # @end, need to check if we reached target, and get the ways

        def check_get_target(num_index, current_sum, cache):
            
            # Now all elements taken
            if num_index >= len(nums):
                # Check @target or not
                if current_sum==target:
                    return 1 #Found 1 way
                else:
                    return 0 # Reached @end and not at target
            
            # Check from cache
            if (num_index, current_sum) in cache:
                return cache[(num_index, current_sum)]

            # Can add to current sum or subtract from it

            # Add to it
            num_ways_add = check_get_target(num_index + 1, current_sum + nums[num_index], cache)

            # Subtract from it
            num_ways_subtract = check_get_target(num_index + 1, current_sum - nums[num_index], cache)

            # Return total ways to reach target from here
            cache[(num_index, current_sum)] = num_ways_add + num_ways_subtract
            return cache[(num_index, current_sum)]

        # Initialise Cache
        # Using a hashmap as a cache can be easier
        return check_get_target(0, 0, {})