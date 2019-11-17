def canConstruct(self, ransomNote, magazine):
        count = 0
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                count = count + 1
            else:
                return False
        if count == len(ransomNote):
            return True