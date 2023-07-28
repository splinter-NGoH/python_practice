# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val) + " " + str(self.left) + " " + str(self.right)


class Solution:
    def allPossibleFBT(self, n: int):
        dp = {0: [], 1: [TreeNode()]}

        def backtracking(n):
            if n in dp:
                return dp[n]
            result = []
            for left in range(n - 1):
                right = n - 1 - left
                print("left", left, "right", right)
                print("before rec", n)
                left_nodes, rightnodes = backtracking(left), backtracking(right)
                print("left_after rec", left_nodes, "right_after rec", rightnodes)
                print("after rec", n)
                for t1 in left_nodes:
                    for t2 in rightnodes:
                        result.append(TreeNode(0, t1, t2))

            dp[n] = result
            print("dp", dp)
            print("dp", dp[n])
            return result

        return backtracking(n)


example = Solution()
n = 7
print(list(example.allPossibleFBT(n)))
