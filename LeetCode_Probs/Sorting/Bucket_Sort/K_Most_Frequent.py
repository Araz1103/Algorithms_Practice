from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Store elements in a dict with their counts -> O(N)
    # If we now sort based on the frequency, we can get
    # But the Sorting takes O(N*LOG(N))
    # We want to give back in O(N)
    
    # We can use Bucket Sort to Sort in O(N)
    # The frequencies are also in a range too

    # Once we have our elements with their frequencies
    # {5: 1, 4: 1, 0: 3, 2: 4, 1: 2}
    # Find min and max of frequencies, that's our range
    # min will be 1 and max will be n (as can't be more than n)
    # {n: #Elements with Frequency n , n-1: .... 1: #Elements with Frequency 1}

    # Our Buckets are from 1 to N
    # {1: [], 2: []......N:[]}
    # Go through the Frequency dict, and use the value (Frequency) to decide the bucket
    # Add the key in our above Bucket Dict
    # Now we can start from N, and keep iterating through values
    # Until we get K elements
    # So if a frquency bucket list above empty, skip

    # O(N)
    frequency_dict = {}
    for num in nums:
        if num not in frequency_dict:
            frequency_dict[num] = 1
        else:
            frequency_dict[num] += 1

    # O(N)
    # Now make the bucket dict
    # Buckets from 1 to N
    bucket_dict = {key: [] for key in range(1, len(nums)+1)}
    for key, frequency in frequency_dict.items():
        bucket_dict[frequency].append(key)

    # Now we need to return Top K keys from bucket dict
    # Starting from N
    top_elements = []
    found_k = False
    # O(N)
    for i in range(len(nums), 0, -1):
        for element in bucket_dict[i]:
            top_elements.append(element)
            # Check if we have k elements
            if len(top_elements)==k:
                found_k = True
                # Can also do return top_elements
            if found_k:
                break
        if found_k:
            break

    return top_elements

    