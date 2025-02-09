"""
We have 2 lists, list1 and list2
We need to remove all elements of list2 from list1, and then return list1
Whichever element of list2 is not in list1, skip it


Inefficient approach is in O(N*M), where len(list2) is N and len(list1) is M

For each element of list2, we check if that is in list1, and if it is, we remove it

Can we do this in O(N) instead of O(N^2)?
"""

def remove_common_elements(list1: list, list2: list) -> list:
    set_list2 = set(list2) # O(N) Time
    new_list = []
    for element in list1: # O(N) Time
        if element not in set_list2: # Set Lookup in O(1)
            new_list.append(element) # Appending to a new list O(1)

    return new_list #Time Complexity is O(N) and Space Complexity is O(N)

# Approach Think

# Let's convert list2 to a set
# That takes O(N) time
# Have a new empty list

# Then if we iterate through list1 ( O(N) Time )
# If element is in set of list2 ( O(1) Time), we continue
# If not, we add it to this new list

print(remove_common_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_common_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_common_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))

print(remove_common_elements([1, 2, 3, 4, 5], [6]))
print(remove_common_elements(["araz", "amol", "sujaan", "chabbi"], ["mama", "aabaa", "araz"]))
print(remove_common_elements([6, 7, 8, 2, 7, 8, 6 ,2], [6, 7, 8, 2]))