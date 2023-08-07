class Solution(object):
    def dailyTemperatures(self, arr):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result_list = [0]*len(arr)
        stack = []

        for i, t in enumerate(arr):
            can_pop = True
            print(i, t)
            while len(stack) > 0 and can_pop:

                if arr[stack[-1]] < t:
                    result_list[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    can_pop = False

            stack.append(i)

        return result_list