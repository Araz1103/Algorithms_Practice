# Designing a Adjacency List

from collections import deque

# GraphNode used for adjacency list
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

# Or use a HashMap
adjList = { "A": [], "B": [] }

# Given directed edges, build an adjacency list
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

# For Coding Interviews we use Hashmap, more convienient
adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)

# Find number of paths from start_node to target_node
# Time Complexity Analysis
# This backtracking is exponential. 
# In the worst case, each node is connected to every other node in the graph. Recall the rule that
# E <= V^2
# So, let us say that each vertex has N edges. 
# If we are to create a decision tree which determines how many vertices can be visited from each vertex,
# and the height of that tree is V, then in the worst case, we will have to do N^V work
# In the worst case scenario, N is equal to V, so the time complexity is O(V^V)
def DFS(start_node, target, adjacency_list, visited):
    if start_node in visited:
        return 0 #No paths from here
    
    if start_node==target:
        return 1 #Found 1 path from here
    
    count = 0
    visited.add(start_node)
    # iterate through neighbours, and explore from them
    for neighbour_node in adjacency_list[start_node]:
        count+=DFS(neighbour_node, target, adjacency_list, visited)
    #BackTrack
    visited.remove(start_node)
    return count

# Standard DFS Traversal, to just explore the graph
# Time complexity is: O(V + E)
# Visits every vertice once and every edge once
def dfs(node, adjacency_list, visited):
    if node in visited:
        return  # Stop if already visited

    print(node)  # Process the node
    visited.add(node)

    # Visit all neighbors
    for neighbor in adjacency_list[node]:
        dfs(neighbor, adjacency_list, visited)

# Example Graph (Adjacency List)
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1],
    4: [1, 5],
    5: [2, 4, 6],
    6: [2, 5]
}

# Check num paths from 0 to 6
print("Num Paths from 0 to 6")
print(DFS(0, 6, graph, set()))

print("Recursive Exploration DFS!")
# Call DFS from node 0
visited = set()
dfs(0, graph, visited)

# Iterative version of above

def iterative_dfs(start, adjacency_list):
    visited = set()
    stack = [start] #LIFO, using Stack
    visited.add(start)

    while stack:
        curr_node = stack.pop() #Gets last element, LIFO
        print(curr_node)

        for neighbour in adjacency_list[curr_node]:
            if neighbour not in visited:
                stack.append(neighbour)
                visited.add(neighbour)

print("Iterative DFS")
iterative_dfs(0, graph)

def iterative_bfs(start, adjacency_list):
    queue = deque()
    visited = set()
    queue.append(start)
    visited.add(start)
    length = 0
    while queue:
        print(f"---------{length}---------")
        for i in range(len(queue)):
            curr_node = queue.popleft()
            print(curr_node)
            for neighbour in adjacency_list[curr_node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        length+=1

print("Iterative BFS")
iterative_bfs(0, graph)

# Find shortest path from start_node to target
def BFS(start_node, target, adjacency_list):
    visited = set()
    queue = deque()
    # Add start_node to queue and mark it visited
    queue.append(start_node)
    visited.add(start_node)

    length = 0
    while queue:
        for i in range(len(queue)):
            curr_node = queue.popleft()

            if curr_node==target:
                return length
            
            for neighbour in adjacency_list[curr_node]:
                # Only add to the queue if not visited
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
        length+=1

    return -1 #If target not found, therefore no path exists!
