from pyparsing import nums


def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    pointer = 0
    for element in nums:
        if element != 0:

            nums[pointer] = element
            pointer += 1
    for zeros in range(pointer, len(nums)):
        nums[zeros] = 0

    return nums


nums = [1, 0, 5, 3, 4, 0, 0, 4]
print(moveZeroes(nums))
