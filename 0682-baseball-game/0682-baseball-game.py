class Solution(object):
    def calPoints(self, operations):
        arr = []

        for i in operations:
            if i.lstrip("-").isdigit():
                arr.append(int(i))
            elif i == "+":
                if len(arr) >= 2:
                    arr.append((arr[-1] + arr[-2]))
            elif i == "D":
                if len(arr) > 0:
                    arr.append(arr[-1] * 2)
            elif i == "C":
                if len(arr) > 0:
                    del arr[-1]

        sum = 0

        for i in arr:
            sum += i
        return sum
