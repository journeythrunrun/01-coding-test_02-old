# 21번_https://www.acmicpc.net/problem/16234
# - 해설
# : 한 요소마다(not visit), '연합' 검사(_4방위 dfs&visit 사용)_값갱신 끝까지함 <-> 나_연결정보만->
#
# - 나
# > 방법
# : 먼저 a~z끝까지 정해라. 길 잃어버린다. 그 방법 끝에서 막히거나, 어차피 위에 겹치거나.
# : > 코드 자세히 적는 생각하다가(길어지다가), 큰그림 흐름 생각 옅어져.
# : 아는 형태의 풀이 코드셋(스피드 스킬셋) 활용하려는 노력 생각 좀
# : 느림
# - 같은연합 끼리 같은 값 할당 가넝

# - 해설
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당  #$ 혼자인 연합도 되나
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: #$ visited(다른 뿌리로 인해 확장되기도) # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    #$ forfor문에서 만약 if문 없이 index를 더했으면 n*n이 나왔을 것임.
    #$ break못 = 특정 뿌리로 인해 다른 요소가 union돼어 -1조건을 통과 못해서 +=1을 덜 하게 됨
    if index == n * n: # 인구 이동 못하는 조건
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)

# - 나

n,l,r=map(int, input().split())
map0=[]
for _ in range(n):
    map0.append(list(map(int, input().split())))
map2=[[]*(n-1) for _ in range(n-1)]
result2=[[]*(n-1) for _ in range(n-1)]

result=[0,0]
map3=[]
def connect():
    #global day #~시작이 함수 안이어도 되나

    # 가로(c+=1) 동
    #~ 접근 1맞겠지
    old= map0[0][0]
    for r in range(len(map0)-1):# [50,30,...] / [
        #old=map0[i][0]
        for c in range(len(map0[0])-1) : # 50 / 30
            # 바로 우측 한 개
            nr, nc = r, c + 1
            if nc > -1 and nc < n and nr > -1 and nr < n:
                # exist_True
                if abs(map0[r][c] - map0[nr][nc]) >= l and abs(map0[r][c] - map0[nr][nc])<= r:
                    connect_c=1#map2[r][c]=1
                else :
                    connect_c=0
            # 바로 아래 한 개
            nr, nc = r+1, c
            if nc > -1 and nc < n and nr > -1 and nr < n:
                # exist_True
                if abs(map0[r][c] - map0[nr][nc]) >= l and abs(map0[r][c] - map0[nr][nc])<= r:
                    connect_r=1#map2[r][c]=1
                else:
                    connect_r=0
            map2[r][c]=(connect_c, connect_r)#map3.append((connect_c,connect_r)) # r*c+개

            #     result[0]=result[0]+map0[i][j]
            #     result[1]+=2 if result[1]==0 else 1
            # old=map0[i][j]

# for 에서 go 하면서 count -> _ 값 갱신하는동안 while 계속
connect()
# 뿌리 인덱스에  더해 가야지
for r in range(len(map0) ):  # [50,30,...] / [
    # old=map0[i][0]

def go(r,c):

    for c in range(len(map0[0]) ):  # 50 / 30
        conn_c, conn_r= map2[r][c]
        did=[False,False]



        nr,nc=r,c
        while map2[nr][nc][0]:
            did[0]=True
            result[0]+=map0[r][c+1]
            result[1]+=2 if result[1]==0 else 1
            nr,nc=r, c+1

        if did[0]==False:
            go(nr,nc)

        while map2[nr][nc][1]:#conn_r:
            did[1] = True
            result[0] += map0[r+1][c]
            result[1] += 2 if result[1] == 0 else 1
            nr,nc=r+1, c
        if did[1]==False:
            go(nr,nc)

# m_other / 근데 위가 더 간단할듯
go(0,0)



def dfs(exist,r,c):
    #$동쪽
    old=map0[r][c]
    nr,nc=r,c+1
    if nc >-1 and nc <n and nr >-1 and nr <n :
        target = abs(old - map0[nr][nc])
        if target >= l and target <= r: # exist_True
            old+map0[nr][nc],num+1
            dfs(T)

        else :

    #남쪽
    nc=r
    nr=c


dfs(0,0) # 부터 검사