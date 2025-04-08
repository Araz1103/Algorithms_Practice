"""
Heap Logic Explained (Step-by-Step)
Why a Heap?
We always want to use the character with the highest remaining frequency first.
A max heap ensures that the most frequent character is always chosen first.
How the Heap Works Here:
Since Python only has a min heap, we insert negative counts so that the most frequent character appears first when popped.
Temporary Holding Mechanism (prev_count, prev_char)
We store the last used character separately to prevent it from being reused immediately.
Before processing the next character, the previously held character (if still available) is pushed back into the heap.
This guarantees that the same character never appears in two adjacent positions.
Final Output Construction
The result is built by popping the most frequent character and appending it.
This process continues until the heap is empty, ensuring a valid rearrangement.

"""
import heapq
from collections import Counter

def reorganizeString(s: str) -> str:
    """
    Rearranges the characters of the string `s` so that no two adjacent characters are the same.
    If such an arrangement is not possible, returns an empty string.
    
    Approach:
    - Use a max heap to always pick the character with the highest remaining frequency.
    - Maintain a temporary hold on the most recently used character to prevent consecutive repetitions.
    """
    # Count the frequency of each character
    freq = Counter(s)
    total_chars = len(s)
    
    # Think logically
    # The only way we cannot have an arrangement where 2 adjacent chars are not same
    # Is when 1 char occurs more than 50% of the total number of chars
    # Even with 50% we can fit
    # But > 50% no arrangement possible
    # So we first get a hashmap of all chars with their frequencies
    # Then iterate through that and check if any char > 50% of (total chars + 1)
    # If it is we return ""
    # Check if the rearrangement is possible
    """
    The key idea is that if any character appears more than half of the time (rounded up) in the string, 
    it’s impossible to rearrange the characters without having two adjacent identical characters.

    Detailed Reasoning:
    Maximum Frequency Constraint:
    For a valid arrangement, the most frequent character (say with frequency X) must be interleaved with the other characters. 
    The best you can do is to place the X occurrences into the “gaps” between the other characters.
    Available Slots Concept:
    Imagine placing all other characters first, which creates gaps before, between, and after them. 
    The maximum number of slots you can create is (total_chars−X+1). 
    To avoid adjacent duplicates, you need: X≤(total_chars−X+1)
    Rearranging: 2X≤total_chars+1
    Which is equivalent to: 2X>total_chars+1(no valid arrangement)
    """
    if any(2 * count > total_chars + 1 for count in freq.values()):
        return ""
    
    # Build a max heap: Python's heapq is a min heap, so we store negative counts.
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)
    
    result = []
    prev_count, prev_char = 0, ""
    
    # Process the heap until it's empty
    while max_heap:
        count, char = heapq.heappop(max_heap)
        # Append the current character
        result.append(char)
        # If there's a previously held character with remaining count, push it back
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))
        
        # Update the count (we used one occurrence)
        count += 1  # since count is negative, adding 1 moves it toward zero
        
        # Hold the current character until the next iteration
        prev_count, prev_char = count, char
    
    return "".join(result)

# Example usage:
print(reorganizeString("aab"))   # Could output: "aba"
print(reorganizeString("aaabc")) # Could output: "abaca" or any valid rearrangement
print(reorganizeString("aaab"))  # Outputs: "" (no valid arrangement)
print(reorganizeString("zzarazaabb"))
print(reorganizeString("baababbb")) # ""
print(reorganizeString("sfffp"))

        