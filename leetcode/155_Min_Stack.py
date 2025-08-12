class MinStack:
    def __init__(self):
        self.cont = []
        self.min = []

    def push(self, val: int) -> None:
        self.cont.append(val)
        val = min(val, self.min[-1] if self.min else val)
        self.min.append(val)

    def pop(self) -> None:
        if len(self.cont) > 0:
            self.cont.pop()
            self.min.pop()

    def top(self) -> int:
        if len(self.cont) == 0:
            return self.cont

        return self.cont[-1]

    def getMin(self) -> int:
        return self.min[-1]
