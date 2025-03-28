
from typing import List
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 2 pointers
    # 1 is iterating through the array
    # 2nd stores the place where the next non-zero element should come
    # Initially that place is at 0index
    # Then everytime a non-zero element is found, we swap at that place, and new place is next to it
    # so non-zero pointer incremented

    non_zero_pntr = 0

    for i in range(len(nums)):
        print(i, nums[i], non_zero_pntr)
        if nums[i]!=0:
            # Swap with non-zero-pntr
            nums[i], nums[non_zero_pntr] = nums[non_zero_pntr], nums[i]
            non_zero_pntr += 1 #Next place where a non-zero element should come
        print(nums)
        print("------------")
    return nums

moveZeroes([0,1,0,3,12])
moveZeroes([0,0,1,0,3,12])
moveZeroes([1,3,12])
        