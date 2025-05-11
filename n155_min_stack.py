class MinStack:
    def __init__(self):
        self.stack = []
        self.stack_diffs = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.stack_diffs.append(min(val, self.stack_diffs[-1] if self.stack_diffs else val))

    def pop(self) -> None:
        self.stack_diffs.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_diffs[-1]


def test_min_stack():
    ms = MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    assert ms.getMin() == -3
    ms.pop()
    assert ms.top() == 0
    assert ms.getMin() == -2
