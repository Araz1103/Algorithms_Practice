import copy

list_of_lists = [[1, 2], [3, 4]]
shallow = list_of_lists.copy()
deep = copy.deepcopy(list_of_lists)

# Modify the original inner list
list_of_lists[0][0] = 99

print(shallow)  # [[99, 2], [3, 4]]  <- Affected by change!
print(deep)     # [[1, 2], [3, 4]]   <- Fully independent
