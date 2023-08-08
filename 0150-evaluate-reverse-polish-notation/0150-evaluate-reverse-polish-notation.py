import math

class Solution:
    def evalRPN(self, arr: List[str]) -> int:
        ans = []

        for i in arr:
            if i == '-':
                second_last_index = len(ans) - 2
                a = ans.pop(second_last_index)
                b = ans.pop()
                print(str(a) + " - " + str(b))
                ans.append(a - b)

            elif i == '/':
                second_last_index = len(ans) - 2
                a = (ans.pop(second_last_index))
                b = (ans.pop())
                print(str(a) + " / " + str(b))
                # val = ((a) / (b))
                # print(val)
                # rounded = math.floor(val)
                # print(rounded, val)
                ans.append(math.trunc((a) / (b)))

                # rounded_towards_zero = math.trunc(number)
                # print(rounded_towards_zero)

            elif i == '+':
                a = (ans.pop())
                b = (ans.pop())
                print(str(a) + " + " + str(b))
                ans.append(a + b)

            elif i == '*':
                a = (ans.pop())
                b = (ans.pop())
                print(str(a) + " * " + str(b))
                ans.append(a * b)

            else:
                ans.append(int(i))

        return ans[0]