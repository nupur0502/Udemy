def lengthOfLastWord(string):
    if not string:
        return 0
    else:
        str_array= string.strip().split(" ")
        len_array = len(str_array)
        len_lastword = len(str_array[len_array-1])
        return len_lastword
print(lengthOfLastWord("Hello World"))