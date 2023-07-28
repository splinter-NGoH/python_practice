import math
class Solution:
    def check(self, dist: list[int], hour: float, speed: int) -> bool:
        time = 0
        for i in range(len(dist) - 1):
            time += math.ceil(dist[i] / speed)
        time += dist[-1] / speed
        return time <= hour
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:
        if hour <= len(dist) - 1:
            return -1
        left, right = 1, 10 ** 7
        while left < right:
            mid = (left + right) // 2
            if self.check(dist, hour, mid):
                right = mid
            else:
                left = mid + 1
        return left
