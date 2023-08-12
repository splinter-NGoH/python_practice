class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(amount - coin + 1):
                dp[i + coin] += dp[i]
        return dp[amount]
