# -*-coding:utf-8-*-
# digits = [0,0]
digits = [1,2,3]
def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    j=0
    for i in digits:
        j+=1
        if (i<0) or (i>9):
            return None
    output = int("".join(map(str,digits)))
    output += 1 #是数字
    output = str(output)
    output2= []
    # print('output', len(output))
    if len(output) < j:
        output2 =[0 for x in range(j-len(output))]
    for i in str(output):
        output2.append(int(i))
    # for i in range(len(output)-1,-1,-1):
    #     output2[-i] = int(output[i])
    print(output2)
plusOne(digits)