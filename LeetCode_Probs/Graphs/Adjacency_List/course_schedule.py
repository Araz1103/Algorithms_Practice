"""
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true
Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false
Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Constraints:

1 <= numCourses <= 1000
0 <= prerequisites.length <= 1000
All prerequisite pairs are unique.
"""
from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Basically convert input lists of list into an adjajency list
        # pair[0] is the key node
        # pair[1] is the neighbor
        # Ensure all nodes get added in the graph with or w/o neighbors so empty list if no neighbors
        # Then start @first node in the graph
        # We keep traversing and stop whenever we encounter a neighbor already in the visited
        # If the count till then is >= num_courses, True else False
        # count only increases when we have finished traversing all neighbors of each node
        # DFS would work here
        
        if not prerequisites:
            return True #If no PreReq, then any num courses can be taken

        preMap = {i:[] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)

        # We will need to run a DFS on all courses in num_courses from 0 to n-1
        # For each of them, run a DFS to check if there is a cycle or not
        # Maintain a visit set
        visited = set()

        def dfs(start_node):
            if start_node in visited:
                return False # Since this was already visited, is a cycle, cannot take courses

            if preMap[start_node]==[]: #Has no pre-req
                return True #Can take this course

            # Otherwise need to check all the prereqs (neighbors) to see can we take those courses
            # Add current node to visited
            visited.add(start_node)
            for neighbor in preMap[start_node]:
                if not dfs(neighbor): return False #Cannot take the current course, if can't take prereqs
            visited.remove(start_node) # back-track complete
            # For ensuring we don't check same courses again, can make this faster
            preMap[start_node] = []
            return True #Can take all pre-reqs, so can take this course

        # Now need to check can we take all courses
        # If any of them false, we return false
        # Also in case Graph is not connected, we will need to check individually
        for course in range(numCourses):
            if not dfs(course): return False

        return True #Can take all the courses in numCourses
            
        