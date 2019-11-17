def firstUniqChar(self, s):
        char_map={}
        index = 0
        for i in range(len(s)):
            if not s[i] in char_map:
                char_map[s[i]] = 1
            else:
                char_map[s[i]] = char_map[s[i]] + 1
        for k in(char_map.keys()):
            if(char_map[k] == 1):
                index = s.index(k)
                return index
        return -1 