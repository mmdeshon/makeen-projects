def Combine_dict(dictA, dictB):
    dictC = {}
    for key_item in dictA.keys():
        if key_item in dictB.keys():
            dictC[key_item] = dictA[key_item] + dictB[key_item]
        else:
            dictC[key_item] = dictA[key_item]
    for key_item in dictB.keys():
        if key_item not in dictC.keys():
            dictC[key_item] = dictB[key_item]

    return dictC

dictA = {'a': 10, 'b': 20, 'c': 30}
dictB = {'a': 3, 'c': 6, 'd': 3}
print(Combine_dict(dictA, dictB))