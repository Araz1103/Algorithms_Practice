# Definition for a pair.

class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

from typing import List
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        starting_pairs = pairs[:]
        insertion_sort_states = [starting_pairs]
        # Handle if empty
        if not pairs:
            return []

        for i in range(1, len(pairs)):
            print(f"IN i: {i}")
            # Check from i till 0th 
            current_index = i
            
            while current_index > 0:
                previous_index = current_index - 1
                print("CI", current_index)
                print("PI", previous_index)
                print(pairs[current_index].key, pairs[previous_index].key)
                if pairs[current_index].key < pairs[previous_index].key:
                    print("Swapping")
                    pairs[previous_index], pairs[current_index] = pairs[current_index], pairs[previous_index]
                    current_index -=1
                else:
                    break # If not greater, then already sorted
            
            current_state = pairs[:]
            insertion_sort_states.append(current_state)
            print(f"At {i}")
            print([[pair.key, pair.value]for pair in insertion_sort_states[i]])
            print([(pair.key, pair.value) for pair in pairs])
            
            print("\n-----------------------\n")

        return insertion_sort_states



        