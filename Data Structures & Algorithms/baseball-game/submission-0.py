class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        stack = []

        for op in operations:
            if op == "C":
                total -= stack.pop()
            elif op == "D":
                val = stack[-1] * 2
                stack.append(val)
                total += val
            elif op == "+":
                val = stack[-1] + stack[-2]
                stack.append(val)
                total += val
            else:
                val = int(op)
                stack.append(val)
                total += val

        return total