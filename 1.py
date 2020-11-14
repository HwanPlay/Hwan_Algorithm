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

    if isUp[idx-1] and isUp[idx+1]: # 좌우 버튼이 올라가 있음, 왼쪽 부모에 연결
      parent_node[idx] = find_parent_node(idx-1)
      parent_node[find_parent_node(idx+1)] = parent_node[idx]
      if isOn[find_parent_node(idx-1)]: #왼쪽이 켜져있음        
        isOn[idx] = True   
        result.append(idx)
      # elif isOn[idx+1]: #오른쪽 이 켜져있음
      #   parent_node[idx] = find_parent_node(idx+1)
      #   parent_node[find_parent_node(idx-1)] = parent_node[idx]

    elif isUp[idx-1]: # 좌 버튼이 올라가 있음
      parent_node[idx] = find_parent_node(idx-1)
      if isOn[find_parent_node(idx-1)]: #왼쪽이 켜져있음
        isOn[idx] = True
        result.append(idx)
    elif idx != len(A) and isUp[idx+1]: # 우 버튼이 올라가 있음
      parent_node[idx] = find_parent_node(idx+1)
      # if isOn[idx+1]: # 오른이 켜져있음
      #   isOn[idx] = True
    else: # 둘다 안올라감
      parent_node[idx] = idx
    print(isOn)
    print(parent_node)
    # if isOnBefore[idx-1]:
    #   isOnBefore[idx] = True
    return len(result)

solution([2, 1, 3, 5, 4])