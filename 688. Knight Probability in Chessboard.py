class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        for _ in range(k):
            dp2 = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    for x, y in [
                        (i - 1, j - 2),
                        (i - 1, j + 2),
                        (i + 1, j - 2),
                        (i + 1, j + 2),
                        (i - 2, j - 1),
                        (i - 2, j + 1),
                        (i + 2, j - 1),
                        (i + 2, j + 1),
                    ]:
                        if 0 <= x < n and 0 <= y < n:
                            dp2[x][y] += dp[i][j] / 8
            dp = dp2
        return sum([sum(row) for row in dp])
