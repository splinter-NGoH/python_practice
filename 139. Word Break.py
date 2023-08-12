class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        def dfs(path):
            if len(path) == len(s):
                res.append(path[:])
                return
            for i in range(len(s)):
                if s[i] in path:
                    continue
                path.append(s[i])
                dfs(path)
                path.pop()

        res = []
        dfs([])
        return res