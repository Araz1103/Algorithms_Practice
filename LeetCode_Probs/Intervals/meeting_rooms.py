"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Example 1:

Input: intervals = [(0,30),(5,10),(15,20)]

Output: false
Explanation:

(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict
Example 2:

Input: intervals = [(5,8),(9,15)]

Output: true
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""


# Definition of Interval:

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True # No conflicts if 0 or 1 meetings

        # First sort all meetings based on their starting times
        intervals.sort(key=lambda x: x.start)

        # Now starting from 2nd meeting, check if it is starting post the previous meeting or not
        # >= end time of last meeting
        for i in range(1, len(intervals)):
            previous_meeting_end = intervals[i-1].end
            current_meeting_start = intervals[i].start
            if current_meeting_start >= previous_meeting_end:
                continue
            else:
                return False

        return True

        
