def bucketSort(arr):
    # Assuming arr only contains 0, 1 or 2
    # Each of these corresponds to 0, 1 and 2
    counts = [0, 0, 0]

    # O(N)
    # Count the quantity of each val in arr
    for n in arr:
        # We keep a track of how many 0s, 1s and 2s are there
        counts[n] += 1
    
    # Now since we know how many 0s, 1s and 2s are there
    # We can create a sorted array, by just adding those many 0s then 1s then 2s
    # Done in O(N)
    # Therefore if our values are in a specific range, sorting works in O(N)
    
    # Fill each bucket in the original array
    i = 0
    for n in range(len(counts)):
        for j in range(counts[n]):
            arr[i] = n
            i += 1
    return arr

print(bucketSort([1, 0, 0, 2, 1, 1, 0]))