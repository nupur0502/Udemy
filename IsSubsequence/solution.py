def isSubsequence(self, s, t):
        index = 0
        length = len(s)

        for c in s:
            charIndex = t.find(c)
            if charIndex < 0:
                return False

            if index == length - 1:
                return True

            t = t[(charIndex + 1):]
            index = index + 1

        return True