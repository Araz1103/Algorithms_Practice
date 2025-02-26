"""
Given an array of integers arr and two integers k and threshold, 
return the number of sub-arrays of size k and average greater than or equal to threshold.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Sub-arrays [2,5,5],[5,5,5] and [5,5,8] have averages 4, 5 and 6 respectively. All other sub-arrays of size 3 have averages less than 4 (the threshold).

Example 2:
Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 sub-arrays of size 3 have averages greater than 5. Note that averages are not integers.
 
Constraints:

1 <= arr.length <= 105
1 <= arr[i] <= 104
1 <= k <= arr.length
0 <= threshold <= 104
"""
# Intuition
# Basically have our window, and calculate average
# When sliding it to next, subtract last and new for fast average calculation
# If exceeds keep a count

def numOfSubarrays(arr, k, threshold):
    """
    :type arr: List[int]
    :type k: int
    :type threshold: int
    :rtype: int
    """
    L = 0
    avg_count = 0
    average = sum(arr[L:(k)])/k
    for R in range(k-1, len(arr)):
        # First check if window size exceeded or not
        if (R - L + 1 > k):
            # From current average subtract L
            # Add new R
            # Get new average
            average = average*k
            average -= arr[L]
            average += arr[R]
            average /= k
            L+=1 # Shift Window!

        if average >= threshold:
            avg_count +=1

    return avg_count

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))

arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(numOfSubarrays(arr, k, threshold))

arr = [7429,3333,9625,3345,6610,6582,1886,9010,8738,5954,8602,5745,7620,2300,4530,5399,8848,1711,9821,3046,8737,3990,2581,5630,1776,1942,416,8718,350,6988,8421,9753,5778,4219,866,2882,5138,4434,7615,326,5219,9008,2468,1182,5958,7360,3358,329,2789,2262,6597,9183,1176,6062,8615,7245,4789,6378,3357,5763,2411,7546,5061,2050,1980,2025,8446,9536,4854,968,8,8038,9192,6316,7156,1845,461,1034,8993,1612,5127,6645,7512,7250,6003,7038,8547,9857,906,663,4727,4642,5916,6293,6148,9915,3059,1337,962,1797,924,4423,5210,5187,8999,5752,3742,769,266,4924,5090,9970,566,4973,752,4607,4635,7715,7577,340,9590,9883,7434,1575,1461,2785,9771,7403,3307,8819,9149,5412,8439,8755,4062,9643,166,2132,7771,4727,1367,5573,5569,1790,449,6608,7283,1350,806,9348,3237,5219,6839,1460,324,5941,4962,8118,7671,1033,8082,7407,4261,6295,5290,9195,867,3237]
k = 68
threshold = 5000
print(numOfSubarrays(arr, k, threshold))


def numOfSubarrays(arr, k, threshold):
    """
    :type arr: List[int]
    :type k: int
    :type threshold: int
    :rtype: List of Sub Arrays
    """
    L = 0
    avg_subarrays = []
    average = sum(arr[L:(k)])/k
    for R in range(k-1, len(arr)):
        # First check if window size exceeded or not
        if (R - L + 1 > k):
            # From current average subtract L
            # Add new R
            # Get new average
            average = average*k
            average -= arr[L]
            average += arr[R]
            average /= k
            L+=1

        if average >= threshold:
            avg_subarrays.append(arr[L:R+1])

    return avg_subarrays

arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
print(numOfSubarrays(arr, k, threshold))

arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 2
print(numOfSubarrays(arr, k, threshold))

arr = [7429,3333,9625,3345,6610,6582,1886,9010,8738,5954,8602,5745,7620,2300,4530,5399,8848,1711,9821,3046,8737,3990,2581,5630,1776,1942,416,8718,350,6988,8421,9753,5778,4219,866,2882,5138,4434,7615,326,5219,9008,2468,1182,5958,7360,3358,329,2789,2262,6597,9183,1176,6062,8615,7245,4789,6378,3357,5763,2411,7546,5061,2050,1980,2025,8446,9536,4854,968,8,8038,9192,6316,7156,1845,461,1034,8993,1612,5127,6645,7512,7250,6003,7038,8547,9857,906,663,4727,4642,5916,6293,6148,9915,3059,1337,962,1797,924,4423,5210,5187,8999,5752,3742,769,266,4924,5090,9970,566,4973,752,4607,4635,7715,7577,340,9590,9883,7434,1575,1461,2785,9771,7403,3307,8819,9149,5412,8439,8755,4062,9643,166,2132,7771,4727,1367,5573,5569,1790,449,6608,7283,1350,806,9348,3237,5219,6839,1460,324,5941,4962,8118,7671,1033,8082,7407,4261,6295,5290,9195,867,3237]
k = 68
threshold = 5000
print(len(numOfSubarrays(arr, k, threshold)))