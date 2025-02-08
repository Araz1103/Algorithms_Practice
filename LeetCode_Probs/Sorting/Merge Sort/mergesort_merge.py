# 2 sorted lists given
# Aim is to merge them into 1 sorted list

# Iterative Approach
def merge_sorted_lists(a, b):
    a_pntr = 0
    b_pntr = 0

    final_sorted = []

    while a_pntr < len(a) and b_pntr < len(b):
        if a[a_pntr] <= b[b_pntr]:
            final_sorted.append(a[a_pntr])
            a_pntr += 1

        else:
            final_sorted.append(b[b_pntr])
            b_pntr +=1

    if a_pntr == len(a):
        final_sorted.extend(b[b_pntr:])
    else:
        final_sorted.extend(a[a_pntr:])

    print(final_sorted)
    return final_sorted


a = [1,2,3,4,5,6]
b = [1,5,6,9,10,13,19,20]
merge_sorted_lists(a, b)


a = [4,5,6]
b = [1,2,3]
merge_sorted_lists(a, b)

# Recursion Approach
