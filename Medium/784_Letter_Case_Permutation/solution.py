class Solution(object):
    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        def backtrack(i, path):
            if i == len(s):
                res.append(path)
                return

            ch = s[i]

            if ch.isdigit():
                backtrack(i + 1, path + ch)
            else:
                backtrack(i + 1, path + ch.lower())
                backtrack(i + 1, path + ch.upper())

        backtrack(0, "")
        return res

