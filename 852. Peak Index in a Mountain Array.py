class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1

        def to_left(idx):
            print(idx)
            print(arr[idx] < arr[idx + 1])
            return arr[idx] < arr[idx + 1]

        while left < right:
            mid = (left + right + 1) // 2   
            print(mid, "mid")
            print(left, right)

            if to_left(mid):
                left = mid

            else:
                right = mid - 1
            print(left, right)
        return left + 1


exarr = [0, 1, 0]
print(Solution().peakIndexInMountainArray(exarr))
