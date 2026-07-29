class Solution(object):
    def isValid(self, s):
        stack = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
                
            elif i == ')':
                if not stack:
                    return False
                if stack.pop() != '(':
                    return False

            elif i == '}':
                if not stack:
                    return False
                if stack.pop() != '{':
                    return False

            elif i == ']':
                if not stack:
                    return False
                if stack.pop() != '[':
                    return False

        return len(stack) == 0