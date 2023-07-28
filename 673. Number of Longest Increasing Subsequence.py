class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        length = len(nums)
        dp = [1] * length
        count = [1] * length
        for i in range(1, length):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
        longest = max(dp)
        return sum([count[i] for i in range(length) if dp[i] == longest])


# i= 1, j= 0, dp[1] = 2, count[1] = 1
# i= 2, j= 0, dp[2] = 2, count[2] = 1
# i= 2, j= 1, dp[2] = 3, count[2] = 1
# i= 3, j= 0, dp[3] = 2, count[3] = 1
# i= 3, j= 1, dp[3] = 3, count[3] = 1
example = Solution()
nums = [1, 3, 5, 4, 7]
print(example.findNumberOfLIS(nums))

for i in range(len(nums) - 1, -1, -1):
    print(i)
