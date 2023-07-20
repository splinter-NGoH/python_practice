def maxArea(height):
    pointer = 0
    pointer1 = len(height) - 1
    maxarea = 0
    while pointer < pointer1:

        maxarea = max(
            maxarea, min(height[pointer], height[pointer1]) * (pointer1 - pointer)
        )
        if height[pointer] < height[pointer1]:
            pointer += 1
        else:
            pointer1 -= 1
    return maxarea


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
