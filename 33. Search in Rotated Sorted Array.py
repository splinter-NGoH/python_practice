class Solution:
    def find_pivot(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left
    def binary_search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left if nums[left] == target else -1
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            return 0 if nums[0] == target else 1 if nums[1] == target else -1
        if nums[0] < nums[-1]:
            return self.binary_search(nums, target)
        else:
            pivot = self.find_pivot(nums)
            if target >= nums[0]:
                return self.binary_search(nums[:pivot], target)
            else:
                return pivot + self.binary_search(nums[pivot:], target)