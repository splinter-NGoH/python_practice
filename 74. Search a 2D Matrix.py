class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_search(arr, target):
            left = 0
            right = len(arr) - 1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] == target:
                    return True

                elif arr[mid] > target:
                    right = mid - 1

                else:
                    left = mid + 1

            return False

        for arr in matrix:
            if binary_search(arr, target):
                return True

        return False