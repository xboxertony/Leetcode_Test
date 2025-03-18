class MinStack:

    ### 如果你 append 的數字不是當下的最小值，不管怎麼 pop 跟 append，都永遠不會是全局最小值

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1]>=val:
            self.min_stack.append(val)

    def pop(self) -> None:
        m = self.stack.pop()
        if m==self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]