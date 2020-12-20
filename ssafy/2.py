import sys
sys.stdin = open('sample_input.txt', 'r')

for tc in range(1, int(input())+1):
    N, R = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    pos_iot = []
    pos_port = []
    for i in range(N):
        for j in range(N):
            if 1 <= arr[i][j] <= 3:
                pos_iot.append([i,j])
            elif arr[i][j] == 9:
                pos_port.append([i,j])


    def find_iot_range(pos_iot):
        map_iot_range = [[[False]*N for _ in range(N)] for _ in range(len(pos_iot))]
        for idx, pos in enumerate(pos_iot):
            x, y = pos
            length = arr[x][y]
            for dx in range(length+1):
                for dy in range(length-dx+1):
                    if 0<=x+dx<N and 0<=y+dy<N:
                        map_iot_range[idx][x+dx][y+dy] = True
                    if 0<=x+dx<N and 0<=y-dy<N:
                        map_iot_range[idx][x+dx][y-dy] = True
                    if 0<=x-dx<N and 0<=y+dy<N:
                        map_iot_range[idx][x-dx][y+dy] = True
                    if 0<=x-dx<N and 0<=y-dy<N:
                        map_iot_range[idx][x-dx][y-dy] = True
        # print(map_iot_range)
        return map_iot_range


    map_iot_range = find_iot_range(pos_iot)
    # print(map_iot_range[0])


    # pos_iot = []
    # pos_port = []
    check_port = [False] * len(pos_port)
    check_iot = [False] * len(pos_iot)
    def isIot(x, y):
        flag = False
        iot_ls = []
        for idx in range(len(pos_iot)):
            if check_iot[idx]:
                continue
            # print(map_iot_range[idx])

            for dx in range(R+1):
                for dy in range(R-dx+1):
                    if (0<=x+dx<N and 0<=y+dy<N and map_iot_range[idx][x+dx][y+dy]) or\
                            (0<=x+dx<N and 0<=y-dy<N and map_iot_range[idx][x+dx][y-dy]) or \
                            (0<=x-dx<N and 0<=y+dy<N and map_iot_range[idx][x-dx][y+dy]) or \
                            (0<=x-dx<N and 0<=y-dy<N and map_iot_range[idx][x-dx][y-dy]):
                        check_iot[idx] = True
                        flag = True
                        iot_ls.append(idx)
                        break
                else:
                    continue
                break
        # print(iot_ls)
        if flag: return True, iot_ls
        return False, iot_ls

    def dfs(Num_Iot, Num_ap, depth, Num_port):
        if Num_Iot == 0:
            global result
            if result > Num_ap:
                result = Num_ap
            return

        if Num_ap == 5:
            return
        if depth == Num_port:
            return
        for idx_port in range(depth, Num_port):
            x, y = pos_port[idx_port]
            flag, iot_idx_ls = isIot(x, y)
            # print(flag,iot_idx_ls)
            if flag:
                for idx_iot in iot_idx_ls:
                    check_iot[idx_iot] = True
                dfs(Num_Iot-len(iot_idx_ls), Num_ap+1, depth+1, Num_port)
                for idx_iot in iot_idx_ls:
                    check_iot[idx_iot] = False
            else:
                dfs(Num_Iot, Num_ap, depth+1, Num_port)

        pass

    result = 0xffff
    dfs(len(pos_iot), 0, 0, len(pos_port))
    if result != 0xffff:
        print('#{} {}'.format(tc, result))
    else:
        print('#{} {}'.format(tc, -1))

