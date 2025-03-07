"""
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
find the minimum number of days required to schedule all meetings without any conflicts.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1
Note:

(0,8),(8,10) is not considered a conflict at 8
Constraints:

0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
"""

from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Basically first sort meetings
        # Then we keep checking which are conflicting or not
        # Till they are not conflicting,they can be done on 1 day
        # The minute they conflict, that meeting needs to be done on another day

        # So initially day 1
        # Keep checking till any conflicts
        # Then as soon as a conflict
        # New day starts, for meetings starting from then
        if len(intervals) <= 1:
            return len(intervals) # Need only 1 day

        intervals.sort(key = lambda x: x.start)

        schedule = [ [intervals[0]] ]

        for i in range(1, len(intervals)):
            previous_meeting_end = intervals[i-1].end
            current_meeting_start = intervals[i].start

            if current_meeting_start >= previous_meeting_end:
                # Can add in the current day
                schedule[-1].append(intervals[i]) 
            else:
                # Either we can add meeting on a new day
                # Or we can check if it can be scheduled on any previous day
                found_day = False
                for day in schedule:
                   last_meeting = day[-1]
                   if current_meeting_start >=last_meeting.end:
                    day.append(intervals[i])
                    found_day = True
                    break
                if not found_day: 
                    # We need a new day to schedule from now
                    schedule.append([intervals[i]])

        #print(schedule)
        return len(schedule)
        
        
# intervals=[(1,5),(2,6),(3,7),(4,8),(5,9)]
# 1 2 3 4 5 
#   2 3 4 5 6
#     3 4 5 6 7
#       4 5 6 7 8
#         5 6 7 8 9

# 1 2 3 4 5 and 5 6 7 8 9 can be done in a previous intervals
# so before incrementing day, we should check if it can be done in a previous interval or not

# 2 Pointers Approach

"""

0 --------------------------- 30
    5---10
        10----15

#numrooms = 0
Starting at 0, we know 1 meeting room is required
#numrooms+=1 (1)
Then at 5, no meeting has ended yet and another meeting room is required
#numrooms+=1 (2)
Then at 10, one meeting has ended
#numrooms-=1 (1)
Then at 10, another meeting has started (we first always check if one has ended or not)
#numrooms+=1 (2)
Then at 15, meeting has ended
#numrooms-=1 (1)
Then at 30, meeting has ended
#numrooms-=1 (0)

So we keep incrementing and decrementing meeting room count, and keep a track of max count which went
This gives us overall how many meeting rooms were required to do all meetings

# 1 2 3 4 5 
#   2 3 4 5 6
#     3 4 5 6 7
#       4 5 6 7 8
#         5 6 7 8 9

If we consider above example also:

1------------------9
#numrooms = 0
1 -------5
   2----------6
     3----------7
       4----------8
         5----------9 

@1 numroom = 1
@2 numrooms = 2
@3 numrooms = 3
@4 numrooms = 4
@5 numrooms-=1 = 3 #meeting finished
@5 numrooms+=1 = 4 #new meeting started
@6 numrooms-=1
@7 numrooms-=1
@8 numrooms-=1
@9 numrooms-=1

So max is 4!
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # We need start and end separately sorted
        # So we can interate through both
        # And update meeting room counts accordingly
        s_times = sorted([i.start for i in intervals])
        e_times = sorted([i.end for i in intervals])

        max_rooms = 0
        num_rooms = 0 #Initially
        # We iterate through start
        # At each start, we first check if an end meeting is done
        # If done, we can increment end time pointer
        e_pointer = 0

        # We just need to go through all start, as post that meeting room count decrements
        for s_time in s_times:
            # First check if current end time is before start time or not
            while e_times[e_pointer] <= s_time:
                num_rooms-=1
                max_rooms = max(num_rooms, max_rooms)
                e_pointer+=1
                if e_pointer == len(e_times):
                    break
            
            # Now we can add a room for this start time
            num_rooms+=1
            max_rooms = max(num_rooms, max_rooms)

        return max_rooms