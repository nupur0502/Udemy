def sliceString(string, start, stop):
    
    start_index = string.index(start)
    last_index = string.rfind(stop)
    new_str = string[:start_index] + string[last_index+5:]    
    return new_str

print(sliceString("Hello my friend I agree to x hs fdkfsk fdskfds dj Hello again my friend this is John","I agree to","Hello"))