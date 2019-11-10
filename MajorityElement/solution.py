def SingleNumber(num):
    num_dic= {}
    for i in range(len(num)):
        if not num[i] in num_dic:
            num_dic[num[i]] = 1
        else:
            num_dic[num[i]] =num_dic[num[i]] + 1
    for i in num_dic.keys():
        if num_dic[i] > int(len(num)/2):
             return i
print(SingleNumber([2,2,1,1,1,2,2]))