import sys
sys.stdin = open('input.txt', 'r')

def solution(A):
  isOn = [True] + [False]*len(A)
  isUp = [True] + [False]*len(A)
  parent_node = [0] * (len(A)+1)
  child_node = [0] * (len(A)+1)
  result = []
  def find_parent_node(idx):
    while parent_node[idx] != idx:
      idx = parent_node[idx]
    return idx

  for idx in A:
    isUp[idx] = True

    if idx != len(A) and isUp[idx-1] and isUp[idx+1]:
      parent_node[idx] = find_parent_node(idx-1)
      parent_node[find_parent_node(idx+1)] = parent_node[idx]
      if isOn[find_parent_node(idx-1)]:     
        isOn[idx] = True   
        result.append(idx)

    elif isUp[idx-1]: 
      parent_node[idx] = find_parent_node(idx-1)
      if isOn[find_parent_node(idx-1)]: 
        isOn[idx] = True
        result.append(idx)
    elif idx != len(A) and isUp[idx+1]: 
      parent_node[idx] = find_parent_node(idx+1)
    else:
      parent_node[idx] = idx
  print(len(result))

solution([1,3,4,2,5])