"""
You have planned some train traveling one year in advance. The days of the year in which you will travel are given as an integer array days. Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.

 

Example 1:

Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.
Example 2:

Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
 

Constraints:

1 <= days.length <= 365
1 <= days[i] <= 365
days is in strictly increasing order.
costs.length == 3
1 <= costs[i] <= 1000
"""
from typing import List
class Solution:
    # Time complexity: O(N), where N is number of days, as only compute once for each day
    # Space complexity is: O(N), where N is number of days, as cache and stack both N
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        def get_min_cost(day_index):

            if day_index >= len(days):
                # Travelled all days
                return 0

            if day_index in cache:
                return cache[day_index]

            # 3 choices
            # Buy a 1 day pass
            # Buy a 7 day pass
            # Buy a 30 day pass

            # 1 day cost
            one_day_pass = costs[0] + get_min_cost(day_index + 1)

            # 7 day cost
            # We will need to check next index for 7 day duration, post current day
            current_day = days[day_index]
            check_index = day_index + 1
            while True:
                # Check if day here in the 7 day pass duration or not
                # Instead of range, can also check days[check_index] < current_day + 7
                if check_index < len(days) and days[check_index] in range(current_day, current_day + 7):
                    # Check next index
                    check_index+=1
                else:
                    # Since day is not or exceeded days, can break and check cost there
                    break
            
            seven_day_pass = costs[1] + get_min_cost(check_index)

            # 30 day cost
            # We will need to check next index for 30 day duration, post current day
            current_day = days[day_index]
            check_index = day_index + 1
            while True:
                # Check if day here in the 30 day pass duration or not
                # Instead of range, can also check days[check_index] < current_day + 30
                if check_index < len(days) and days[check_index] in range(current_day, current_day + 30):
                    # Check next index
                    check_index+=1
                else:
                    # Since day is not or exceeded days, can break and check cost there
                    break
            
            thirty_day_pass = costs[2] + get_min_cost(check_index)

            cache[day_index] = min(one_day_pass, seven_day_pass, thirty_day_pass)
            return cache[day_index]

        return get_min_cost(0)
                

        