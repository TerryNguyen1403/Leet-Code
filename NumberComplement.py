def numberComplement(num):
    dic = []
    binary = bin(num)[2:]

    for i in range(len(binary)):
        if binary[i] == '1':
            dic.append('0')
        else:
            dic.append('1')

    int_value = "".join(dic)
    result = int(int_value, 2)

    return result
