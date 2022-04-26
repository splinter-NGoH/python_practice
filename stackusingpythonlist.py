class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return print("{} the elemnt add successfully".format(self.list[-1]))

    def pop(self):
        if self.is_empty():
            return "there is no more elements here"

        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            return "no elemnts here"

        else:
            self.list[len(self.list[-1])]


customstack = Stack()
customstack.push(2)
