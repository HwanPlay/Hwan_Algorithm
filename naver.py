def sol1():
    ls = list(range(1, 101))
    ls.remove(59)
    res = sum(range(1, 101))

    return res-sum(ls)

print(sol1())
# sum_val = sum(range(1,101))
# ls = [1,2, 4, ... 100]
# result = sum_val - sum(ls)
#
# randomized_list = []

def solution(string):
    N = len(string)
    for idx in range(N//2):
        if string[idx] != string[N-idx-1]:
            return False
    return True

print(solution('a2a'))

def sortByOrder(idSortOrder, objectArray):
    '''
    var idSortOrder = ['a','b','c','d','e']
    var objectArray = [
        {id: 'e', value: '_e'},
        {id: 'b', value: '_b'},
        {id: 'c' , value: '_c'},
        {id: 'a' , value: '_a'},
        {id: 'd', value: '_d'}
    ]
    '''
    result = []
    # for sort_key in idSortOrder:
    #     result.append(dict(sort_key=objectArray[sort_key]))
    # return result
    dict_order = {}
    for idx, order in enumerate(idSortOrder):
        dict_order[order] = idx
    result = [0]*len(idSortOrder)
    for val in objectArray:
        result[dict_order[val.id]] = f'id:{val.id}, value:{val.value}'
        # result[4] = '{id: 'e', value: '_e'}'
    return result
