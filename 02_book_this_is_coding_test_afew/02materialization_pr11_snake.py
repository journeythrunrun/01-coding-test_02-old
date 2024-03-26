# 1. 문제 : 뱀
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
n = int(input())
k = int(input())

apple = []
for i in range(k):
    # 행, 열 좌표로 입력 준대
    apple.append(list(map(int, input().split())))
    apple[i][0] -= 1  ## -1
    apple[i][1] -= 1  ## -1

l = int(input())
turn = []
for i in range(l):
    turn.append(list(map(str, input().split())))  # str ["12" 'D"]

    # t초 후 L or D로 회전
map = [[0] * n for _ in range(n)]

# 사과 위치시키기
for i in range(k):
    map[apple[i][0]][apple[i][1]] = 1

# !가져다쓰면[행_y세로][열_x가로] -> 인덱스용 변수 저장, 가져다 쓸때 [1]<->[0]
# ->걍 dx dy해라
d = [[0, 1], [-1, 0], [0, -1], [1, 0]]  # 동 북 서 남 #X_[notx, noty]_d= [[1,0],[-1,0],[1,0],[0,1]]
present = [0, 0]
go = d[0]
go_index = 0
map[0][0] = 2  # 뱀 몸=2

bem = []  # append & pop(0)
# heapq.push(tail, (count,[0,0])) # count=0
t = 0
bem.append(present[:])

while (1):  # 뱀 몸=2
    # 방향 전환
    if len(turn) > 0 and t == int(turn[0][0]):
        if turn[0][1] == 'L':
            go_index += -3 if go_index == 3 else 1

        else:
            go_index += +3 if go_index == 0 else -1
        go = d[go_index]
        turn.pop(0)
    # 이동 (L or D) 및 new 위치!
    t += 1
    present = [a + n for a, n in zip(present, go)]  # new =[go[i]+present[i] for i in len(go)]
    bem.append(present[:])  # !present_새위치후 뱀 머리 위치 업데이트_머리 먼저 들이밀고 break체크 #~

    # [ 1,0 ] -> 2
    # print(map)
    if present[0] >= 0 and present[0] <= n - 1 and present[1] >= 0 and present[1] <= n - 1:  # try :
        new_visit = map[present[0]][present[1]]
    else:  # except :#! 인덱스에러_초과시에만 발생하고 음수는 계산돼버림 주의. # 벽 부딪힐 케이스
        break

    if new_visit == 1:  # 사과가 있음
        map[present[0]][present[1]] = 2  #! new_visit =2

    elif new_visit == 0:  # 사과가 없음
        map[present[0]][present[1]] = 2  #!new_visit=2
        # tail제거
        # [1]_디버깅용 출력
        erase = bem.pop(0)  # ~ 이미 비었으면#heapq.pop(tail)
        map[erase[0]][erase[1]] = 0
        # [2]_디버깅용 출력
    else:  # new_visit==2 or  # 자기몸
        break
print(t)

# [1]_디버깅용 출력
# print(t, "초 초기 머리만 넣은 모습.------------")
# for i in range(len(map)):
#     for j in range(len(map[0])):
#         print(map[i][j], end='')
#     print()
# # [2]_디버깅용 출력
# print(t, "초 까지의 모습. 머리 방향전환은 t초 '후' ------after------")
# for i in range(len(map)):
#     for j in range(len(map[0])):
#         print(map[i][j], end='')
#     print()




# # - 해설, 내 주석_#$
# n=int(input())
# k= int(input())
# data=[[0]*(n+1) for _ in range(n+1)] # 맵 정보
# info=[] # 방향 회전정보
#
# # 맵정보(사과 있는 곳은 1로 표시)
# for _ in range(k):
#     a,b=map(int, input().split())
#     data[a][b]=1 #$ 코드 간단화_입력 받을 때 맵 업데이트
#
# # 방향 회전 정보 입력
# l=int(input())
# for _ in range(l):
#     x,c=input().split()
#     info.append((int(x),c)) #$ 코드간단화_나중에 int로 바꿔서 쓰는 것보다, 입력단계를 두 단 계로 나눠서 미리 int저장
#
# # 처음에는 오른쪽을 보고 있으므로 (동, 남, 서, 북)
# dx=[0,1,0,-1]
# dy=[1,0,-1,0] #$ 각각_a[b[ index의 index 사용하지 않아도됨<-> 나: 합체
#
# def turn(direction, c): #$ <->go_index
#     if c=="L":
#         direction=(direction-1)%4 #$ 이게 더 간단<->나 : if컴프리헨션 # -1%4=3이네
#     else:
#         direction=(direction+1)%4
#     return direction
#
# def simulate():
#     x,y=1,1 # 뱀의 머리 위치 #$ <-> 나 : x,y를 0부터_다 인덱스로 씀
#     data[x][y]=2 # 뱀이 존재하는 위치는 2로 표시
#     direction=0 # 처음에는 동쪽을 보고 있음
#     time=0 # 시작한 뒤에 지난 '초' 시간
#     index=0 # 다음에 회전할 정보
#     q=[(x,y)] # 뱀이 차지하고 있는 위치 정보 (꼬리가 앞쪽) #$ 인덱스상 앞 : 먼저 입력된 위치이자 꼬리쪽
#
#     while True :
#         nx=x+dx[direction] #$ next_x (( d[go_in_dex))
#         ny=y+dy[direction]
#         # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
#         if 1<= nx and nx<=n and 1<=ny and ny<=n and data[nx][ny]!=2: #$<-> try_index except_break
#             # 사과가 없다면 이동 후에 꼬리 제거
#             if data[nx][ny]==0:
#                 data[nx][ny]=2 #$ 방문체크
#                 q.append((nx,ny))
#                 px, py = q.pop(0)
#                 data[px][py]=0
#             # 사과가 있다면 이동 후에 꼬리 그대로 두기
#             if data[nx][ny] ==1:
#                 data[nx][ny]=2
#                 q.append((nx,ny))
#         # 벽이나 뱀의 몸통과 부딪혔다면
#         else :
#             time+=1
#             break
#         x,y=nx,ny # 다음 위치로 머리를 이동
#         time+=1
#         if index<l and time==info[index][0]: #회전할 시간인 경우 회전
#             direction=turn(direction,info[index][1]) #$go_index / LorR
#             index+=1
#     return time
#print(simulate())


# - 나
# 50m (며칠 후에 이어서 푸느라 문제랑 코드 다 다시 본 시간도)
# 1번 맞추고, 2,3번은 16에서 끝나버리네 -> 오래 걸려서 수정완성
# - 오답원인
# ! 인덱스에러_초과시에만 발생하고 음수는 계산돼버림 주의.
# !가져다쓰면[행_y세로][열_x가로] -> 인덱스용 변수 저장, 가져다 쓸때 [1]<->[0]
# ->걍 dx dy해라



