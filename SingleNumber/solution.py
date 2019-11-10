def SingleNumber(num):
    num_dic= {}
    for i in range(len(num)):
        if not num[i] in num_dic:
            num_dic[num[i]] = 1
        else:
            num_dic[num[i]] =num_dic[num[i]] + 1
    print(num_dic)
    for i in num_dic.keys():
        if num_dic[i] == 1:
            return i
print(SingleNumber([4,1,2,1,2]))