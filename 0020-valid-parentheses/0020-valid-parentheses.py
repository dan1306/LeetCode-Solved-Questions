class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
      """

        stack = []

        closing = [')', '}',  ']']

        closing_paranthesis = {
            ')':  '(',
            '}': '{',
            ']': '['
        }

        for i in s:
            if i in closing and len(stack) > 0:
                if stack[-1] == closing_paranthesis[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        if len(stack) > 0:
            return False
        
        return True