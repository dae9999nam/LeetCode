class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s or len(s) == 1:
            return False
        stack = []
        for p in s:
            if p == "(":
                stack.append(")")
            elif p == "[":
                stack.append("]")
            elif p == "{":
                stack.append("}")
            else:
                if not stack:
                    return False
                paranthesis = stack.pop()
                if p != paranthesis:
                    return False
        if stack != []:
            return False
        return True