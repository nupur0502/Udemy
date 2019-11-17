def numMatchingSubseq(self, s, word):
        count = 0
        for i in range(len(word)):
            index = 0
            charindex = 0
            s_in_loop = s
            length = len(word[i])
            for c in word[i]:
                charindex = s_in_loop.find(c)
                if charindex < 0:
                    break

                if index == length - 1:
                    count = count + 1
                else:
                    s_in_loop = s_in_loop[(charindex + 1):]
                    index = index + 1
        return count