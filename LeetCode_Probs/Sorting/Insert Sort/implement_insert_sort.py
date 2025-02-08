"""
Idea of Insertion Sort is to iterate through the list, and check if the current element is < it's left neighbour
If it is, we swap it, and check again if the current element < it's left neighbour
We keep doing until either there is no left neighbour to compare or it is >= left neighbour
This way, for each current element, the elements on the left remain sorted @all times

Example: 2, 5, 3, 1, 4, 0

"" -> Indicates the sorted sub-list @each iteration

A. Start at 2, 2 has no left neighbours so unaffected

-> "2", 5, 3, 1, 4, 0

B. Now 2nd element is 5, but 5 > 2, so unaffected

-> "2, 5", 3, 1, 4, 0

C. 3rd element is 3, 3 < 5, so swap

-> "2, 3, 5", 1, 4, 0

3 is > 2, so unaffected

D. 4th element is 1, 1 < 5, so swap

-> "2, 3, 1, 5", 4, 0

1 < 3, so swap

-> "2, 1, 3, 5", 4, 0

1 < 2, so swap

-> "1, 2, 3, 5", 4, 0

1 has no more left neighbours, so unaffected now

E. 5th element is 4, 4 > 5, so swap

-> "1, 2, 3, 4, 5", 0

4 > 3, so unaffected now

F. 6th elemet is 0, 0 < 5, so swap

-> "1, 2, 3, 4, 0, 5"

0 < 4, so swap

-> "1, 2, 3, 0, 4, 5"

0 < 3, so swap

-> "1, 2, 0, 3, 4, 5"

0 < 2, so swap

-> "1, 0, 2, 3, 4, 5"

0 < 1, so swap

-> "0, 1, 2, 3, 4, 5"

0 has no left neighbours, so unaffected

Finally we have our sorted array!

Time Complexity is O(n^2)
As, for each element in list of n (outerloop)
We have to shift elements to insert, until ith place

Worst case, for a reversed sorted list, we have to do for the nth place, n swaps

so while loop runs, 1 time for i = 1, 2 times for i = 2.... i = n - 1, n-1 times
so total operations: 1 + 2 + 3..... + (n-1)
-> n*(n-1)/2 = n^2

Best case when it is already sorted, so just runs 1 loop
So O(n)
"""


# Approach I
# You have a sorted/unsorted input array
# Initialise an empty array: keep_sorted_array
# You start @beginning, iterate through elements:
# If keep_sorted_array is empty -> add the element to it
# If it is not empty
# Check from the @end in keep_sorted_array: 
# If element < sorted_element: Keep going back
# If element >= sorted_element: Insert it @that position

def insert_sort(input_list):
    keep_sorted_array = []

    for element in input_list:
        if not keep_sorted_array:
            keep_sorted_array.append(element)
        else:
            # Check if element is >= last element, so don't bother checking from beginning
            # Can directly append to sorted list
            if element >= keep_sorted_array[-1]:
                keep_sorted_array.append(element)

            else:
                # Can iterate from @end or beginning, same thing, just check conditions
                for idx, sorted_element in enumerate(keep_sorted_array):
                    if element >= sorted_element:
                        continue #You move on to check the next
                    else:
                        # Insert it @this index
                        # Python insert, adds element @index, and shifts others to right
                        # So insert @0, will shift the current 0th element to the right
                        # Insert @-1 (end) will add it at end, and shift the last element to the right
                        # So insert adds one before the current element present at this index
                        keep_sorted_array.insert(idx, element)
                        # Can break now
                        break

    return keep_sorted_array


print(insert_sort([1, 2, 4, 3, 5, 7 ,6]))
print(insert_sort([1, 2, 3, 5, 6]))
print(insert_sort([1, -2, 3, 5, -6]))

# Approach II
# Sorting in place, so no extra list

def insertion_sort(arr):
    print("arr ip", arr)
    for i in range(1, len(arr)):  # Start from the second element, as first one has nothing to compare on left
        # Basically, keep comparing current element with it's left
        # If current element < left, then we swap those too
        # Otherwise it is at the right place
        # So check until j is less than 0 (no more elements on left) or current element > element @left
        current_element = arr[i]
        j = i - 1
        # j helps us check to the left
        print("current element", current_element)
        print("j is", j)
        while j >= 0 and current_element < arr[j]:
            print("Swapping")
            # Swap current element and the one @left
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -=1
            print("New Arr", arr)
            print("j is", j)
        
    return arr  # Since it's modified in-place

#print(insertion_sort([1, 2, 4, 3, 5, 7 ,6]))
# print(insertion_sort([1, 2, 3, 5, 6]))
print(insertion_sort([1, -2, 3, 5, -6]))

def insertion_sort_reverse(arr):
    print("arr ip", arr)
    for i in range(1, len(arr)):  # Start from the second element, as first one has nothing to compare on left
        # Basically, keep comparing current element with it's left
        # If current element > left, then we swap those too (as we want decreasing order, so max to the left)
        # Otherwise it is at the right place
        # So check until j is less than 0 (no more elements on left) or current element < element @left
        current_element = arr[i]
        j = i - 1
        # j helps us check to the left
        print("current element", current_element)
        print("j is", j)
        while j >= 0 and current_element > arr[j]:
            print("Swapping")
            # Swap current element and the one @left
            arr[j + 1], arr[j] = arr[j], arr[j + 1]
            j -=1
            print("New Arr", arr)
            print("j is", j)
        
    return arr  # Since it's modified in-place

#print(insertion_sort([1, 2, 4, 3, 5, 7 ,6]))
# print(insertion_sort([1, 2, 3, 5, 6]))
print(insertion_sort_reverse([1, -2, 3, 5, -6]))