class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr = []
        for i in tokens:
            if i not in ["+","-","*","/"]:
                arr.append(int(i))
            else:
                a = arr.pop()
                b = arr.pop()
                if i=="+":
                    arr.append(a+b)
                elif i=="-":
                    arr.append(b-a)
                elif i=="*":
                    arr.append(a*b)
                else:
                    arr.append(int(b/a))
        return arr[0]