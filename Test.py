#Count the number of prime numbers less than a non-negative number, n.

#Example:

#Input: 10
#Output: 4
#Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
def vowel(s):
    v = ["a","e","i","o","u"]
    s= s.lower()
    new_s = []
    for i in range(len(s)):
       if s[i] in v:
           new_s = new_s + s[i]
    for i in range(len(s)): hello eo
        if s[i] in v:
            j = 0
            s[i] = new_s[len(new_s)-j]
            j = j +1
    return s
print(vowel("hello"))
    
    