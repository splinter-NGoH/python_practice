class Solution:
    def __init__(self):
        self.I = 1
        self.V = 5
        self.X = 10
        self.L = 50
        self.C = 100
        self.D = 500
        self.M = 1000
        self.counter = 0
        self.list1 = []

    def __str__(self) -> str:
        return str(self.counter)

    def romanToInt(self, s: str) -> int:
        self.list1[:0] = s
        self.stringiter = iter(self.list1)
        for char in self.stringiter:
            if char == "I":

                if len(self.list1) > self.list1.index("I") + 1:
                    if self.list1[self.list1.index("I") + 1] == "V":
                        self.counter += 4
                        next(self.stringiter)

                    elif self.list1[self.list1.index("I") + 1] == "X":
                        self.counter += 9
                        next(self.stringiter)

                    else:
                        self.counter += self.I
                else:
                    self.counter += self.I
            if char == "V":
                self.counter += self.V

            if char == "X":
                if len(self.list1) > self.list1.index("X") + 1:

                    if self.list1[self.list1.index("X") + 1] == "L":
                        self.counter += 40
                        next(self.stringiter)

                    elif self.list1[self.list1.index("X") + 1] == "C":
                        self.counter += 90
                        next(self.stringiter)

                    else:
                        self.counter += self.X
                else:
                    self.counter += self.X
            if char == "L":
                self.counter += self.L

            if char == "C":

                if len(self.list1) > self.list1.index("C") + 1:
                    if self.list1[self.list1.index("C") + 1] == "D":
                        self.counter += 400
                        next(self.stringiter)

                    elif self.list1[self.list1.index("C") + 1] == "M":
                        self.counter += 900
                        next(self.stringiter)

                    else:
                        self.counter += self.C
                else:
                    self.counter += self.C
            if char == "D":
                self.counter += self.D

            if char == "M":
                self.counter += self.M
        return self.counter


romanclass = Solution()
print(romanclass.romanToInt("IM"))
print(romanclass)
