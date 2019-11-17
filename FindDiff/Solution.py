def findTheDifference(self, s, t):
        flag = 0
        s_in_loop = s
        output = ""
        count = 0
        for i in range(len(t)):
            flag = s_in_loop.find(t[i])
            if flag<0:
                count = count + 1
                output = t[i]
            s_in_loop = s_in_loop[(flag+1):] + s_in_loop[:flag]
        if count == 1:
            return output