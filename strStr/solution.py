def strStr(haystack, needle):
    if len(needle) == 0:
        return 0
    index = 0
    if needle in haystack:
        index = haystack.index(needle)
        return index
    else:
        return -1
print(strStr("llhello","o"))