"""
There are two types of soup: type A and type B. Initially, we have n ml of each type of soup. There are four kinds of operations:

Serve 100 ml of soup A and 0 ml of soup B,
Serve 75 ml of soup A and 25 ml of soup B,
Serve 50 ml of soup A and 50 ml of soup B, and
Serve 25 ml of soup A and 75 ml of soup B.
When we serve some soup, we give it to someone, and we no longer have it. Each turn, we will choose from the four operations with an equal probability 0.25. If the remaining volume of soup is not enough to complete the operation, we will serve as much as possible. We stop once we no longer have some quantity of both types of soup.

Note that we do not have an operation where all 100 ml's of soup B are used first.

Return the probability that soup A will be empty first, plus half the probability that A and B become empty at the same time. Answers within 10-5 of the actual answer will be accepted.

 
 """


class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 5000:
            return 1.0
        n = (n + 24) // 25
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 0.5
        for i in range(1, n + 1):
            dp[0][i] = 1
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[i][j] = 0.25 * (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][max(0, j - 1)] + dp[max(0, i - 2)][max(0, j - 2)] + dp[max(0, i - 1)][max(0, j - 3)])
        return dp[n][n]