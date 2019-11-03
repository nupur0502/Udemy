def plusone(number):
    string= ""
    output_arr = []
    for i in range(len(number)):
         string = string + str(number[i])
    string = str(int(string) +1)
    for i in range(len(string)):
        output_arr.append(string[i])
    return output_arr

print(plusone([4,3,2,1])) 