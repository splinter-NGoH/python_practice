class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        def dfs(path):
            if len(path) == len(digits):
                res.append(path[:])
                return
            for i in range(len(digits)):
                if digits[i] in path:
                    continue
                path.append(digits[i])
                dfs(path)
                path.pop()

        res = []
        dfs([])
        return res