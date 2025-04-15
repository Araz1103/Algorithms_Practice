"""
Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

You may return the answer in any order.

Note: Intervals are non-overlapping if they have no common point. 
For example, [1, 2] and [3, 4] are non-overlapping, but [1, 2] and [2, 3] are overlapping.

Example 1:
Input: intervals = [[1,3],[1,5],[6,7]]
Output: [[1,5],[6,7]]

Example 2:
Input: intervals = [[1,2],[2,3]]
Output: [[1,3]]

Constraints:
1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= start <= end <= 1000
"""
from typing import List
class Solution:
    # TC: O(N*Log(N))
    # SC: O(N) for storing intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the Intervals from starting value
        # Then keep comparing with next/previous
        # If overlap, merge and then keep checking with merged one

        if len(intervals)==1:
            return intervals

        intervals.sort(key=lambda x: x[0]) #sort from starting
        merged_intervals = []
        prev_interval = intervals[0]
        idx = 1
        while idx < len(intervals):
            curr_interval = intervals[idx]
            if prev_interval[1] >= curr_interval[0]:
                # merge and update prev interval
                # We know start will be the starting point of prev interval
                # End can be maximum end from both
                end = max(curr_interval[1], prev_interval[1])
                merged_interval = [prev_interval[0], end]
                prev_interval = merged_interval
            else:
                # Since cannot merge, add prev interval to merged_intervals list
                # Update prev interval
                merged_intervals.append(prev_interval)
                prev_interval = curr_interval

            idx+=1
        #@end add the last prev interval to list
        merged_intervals.append(prev_interval)
        return merged_intervals



        