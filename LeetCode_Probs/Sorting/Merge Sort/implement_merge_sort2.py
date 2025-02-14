def merge_sort(start_index, end_index, arr):
    # print("SI", start_index)
    # print("EI", end_index)
    print("Focus Arr", arr[start_index:end_index+1])
    if start_index >= end_index:
        return arr
    
    mid_point = int((start_index + end_index)/2)
    #print("MP", mid_point)

    merge_sort(start_index, mid_point, arr)
    merge_sort(mid_point + 1, end_index, arr)
    merge_sorted_arrays(start_index, mid_point, end_index, arr)
    return arr


def merge_sorted_arrays(start_index, mid_point, end_index, arr):
    print("Merging!")
    # print("SI", start_index)
    # print("EI", end_index)
    # print("MP", mid_point)
    print("Focus Arr", arr[start_index:end_index+1])
    arr1 = arr[start_index:mid_point+1]
    arr2 = arr[mid_point+1:end_index+1]
    print("arr1", arr1)
    print("arr2", arr2)
    arr1_pointer = 0
    arr2_pointer = 0
    add_arr_pointer = start_index
    
    while arr1_pointer < len(arr1) and arr2_pointer < len(arr2):
        arr1_val = arr1[arr1_pointer]
        arr2_val = arr2[arr2_pointer]
        if arr1_val  <= arr2_val:
            arr[add_arr_pointer] = arr1_val
            arr1_pointer +=1
            add_arr_pointer +=1
        else:
            arr[add_arr_pointer] = arr2_val
            arr2_pointer +=1
            add_arr_pointer +=1

    if arr1_pointer == len(arr1):
        for val in arr2[arr2_pointer:]:
            arr[add_arr_pointer] = val
            add_arr_pointer +=1
    else:
        for val in arr1[arr1_pointer:]:
            arr[add_arr_pointer] = val
            add_arr_pointer +=1

    print("MS Arr", arr)
    return arr

print(merge_sort(0, 6, [15,12,11,18,13,1,0]))
# print(merge_sort(0, 4, [15,12,11,18,13]))
# print(merge_sort(0, 3, [1,2,3,4]))
# print(merge_sort(0, 3, ["a","r","a","z"]))
