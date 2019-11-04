count = 0
    length = len(array)
    while(count<k):
        array.insert(0,array[length-1])
        del array[length]
        count = count + 1
    print(array)