class Solution(object):
    def backspaceCompare(self, s, t):
        stack = []
        stack2 = []
        for i in range(len(s)):
            if s[i]=="#":
                if len(stack)>0:
                    stack.pop()
            else:
                stack.append(s[i])
        for i in range(len(t)):
            if t[i]=="#":
                if len(stack2)>0:
                    stack2.pop()
            else:
                stack2.append(t[i])
        return stack2==stack
