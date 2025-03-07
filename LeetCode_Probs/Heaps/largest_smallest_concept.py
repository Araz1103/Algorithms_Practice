"""
Important: 
To have K Largest Elements, we will have a 'Min Heap' of Size K

If 1 2 2 3 4 6

For 3 largest elements, maintain a min heap:

min left right
3    4    6

Now if a new element comes and is < min, ignore (as won't affect 3 largest elements)
Now if a new element comes and is >= min, pop min and push the new element in this heap

If 0 comes: Ignore

If 5 comes:

4  6  5

@any given time, min of this heap gives 3rd largest element overall and all elements of this heap give the 3 largest elements


To have K Smallest Elements, we will have a 'Max Heap' of Size K

If 1 2 2 3 4 6

For 3 smallest elements, maintain a max heap:

max left right
2    2    1

Now if a new element comes and is > max, ignore (as won't affect 3 smallest elements)
Now if a new element comes and is <= max, pop max and push the new element in this heap

If 0 comes:

2  1  0

If -2 comes:

1  0  -2

@any given time, max of this heap gives 3rd smallest element overall and all elements of this heap give the 3 smallest elements
"""