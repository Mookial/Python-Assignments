def rev(lst):
    "returns a copy of list reversing the order. cant use reverse or slice"
    i = len(lst)-1
    xist = []
    while (i >= 0):
        xist.append(lst[i])
        i -= 1
    return xist

#########################################################

def assoc(lst1, lst2):
    """takes 2 equal length lists and returns assoc list.
    if l1 is [1] and l2 is [a] then assoc is [1, a]"""
    lst3 = []
    for i in range (len(lst1)):
        lst3.append(handler(lst1[i], lst2[i]))

    return lst3
    
#########################################################

def handler(a, b):
    "take both lists' value and sends them back in a list"
    list = [a, b]
    return list
