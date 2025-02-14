def merge_sort(start_index, end_index, arr):
    print("SI", start_index)
    print("EI", end_index)
    print("Arr", arr)
    if start_index == end_index:
        return [arr[start_index]]
    
    mid_point = int((start_index + end_index)/2)
    print("MP", mid_point)

    sorted_arr1 = merge_sort(start_index, mid_point, arr)
    sorted_arr2 = merge_sort(mid_point + 1, end_index, arr)
    return merge_sorted_arrays(sorted_arr1, sorted_arr2)

def merge_sort(arr):
    start_index = 0
    end_index = len(arr) - 1
    print("SI", start_index)
    print("EI", end_index)
    print("Arr", arr)
    if start_index == end_index:
        return [arr[0]]
    
    mid_point = int((start_index + end_index)/2)
    print("MP", mid_point)

    sorted_arr1 = merge_sort(arr[start_index:mid_point+1])
    sorted_arr2 = merge_sort(arr[mid_point+1:])
    return merge_sorted_arrays(sorted_arr1, sorted_arr2)

def merge_sorted_arrays(arr1, arr2):
    print("arr1", arr1)
    print("arr2", arr2)
    arr1_pointer = 0
    arr2_pointer = 0
    merge_sorted_arr = []

    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
        arr1_val = arr1[arr1_pointer]
        arr2_val = arr2[arr2_pointer]
        if arr1_val  <= arr2_val:
            merge_sorted_arr.append(arr1_val)
            arr1_pointer +=1
        else:
            merge_sorted_arr.append(arr2_val)
            arr2_pointer +=1

    if arr1_pointer == len(arr1):
        merge_sorted_arr.extend(arr2[arr2_pointer:])
    else:
        merge_sorted_arr.extend(arr1[arr1_pointer:])

    print("MS Arr", merge_sorted_arr)
    return merge_sorted_arr

#print(merge_sort(0, 4, [15,12,11,18,13]))
print(merge_sort([15,12,11,18,13]))
print(merge_sort([1,2,3,4]))
print(merge_sort(["a","r","a","z"]))
