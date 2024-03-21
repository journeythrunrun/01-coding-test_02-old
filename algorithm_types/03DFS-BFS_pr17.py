# https://www.acmicpc.net/problem/18405
# - 해설
from collections import deque

n,k=map(int,input().split())
graph=[]
viru=[]

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n): # 입력 줄 씩 넣을 때 그 줄의 요소 값 검사
        if graph[i][j]!=0:
            viru.append((graph[i][j],0,i,j))# 시간

viru.sort()
q=deque(viru) # 리스트를 넣을 수도 있네

target_s, target_x, target_y=map(int,input().split())
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# bfs
# &이 앞부분을 못했네

# [for제거]for로 될 것들, 데이터 구조에 병렬로 집어넣어버리기
while q:
    virus,s,x,y=q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
    if s==target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        # 해당 위치로 이동할 수 있는 경우
        if 0 <=nx and nx<n and ny<n and 0<=ny :
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus, s+1,nx,ny))
print(graph[target_x-1][target_y-1])


# # 1. 문제 :
# # 2.3. 아이디어 : 코테용 종이로 씀
# # 4. 코딩
#
# # 입력
# # - 나_인데 거의 해설 따라한
# from collections import deque
# n,k=map(int, input().split())
# map0=[]
# for _ in range(n):
#     map0.append(list(map(int,input().split())))
# s,x,y=map(int,input().split()) #변수 x, y 안 겹치게
# biru=[]
# #biru=[[] for _ in range (k+1)]# index_바이러스번호 / 값=(ri,ci)
# for i in range(n):
#     for j in range(n):
#         target=map0[i][j]
#         if target!=0:
#             biru.append((target,0,i,j))
# biru.sort() # [ [ (ri,ci) ], ]
# nbiru=deque(biru)
#
# dr=[-1,1,0,0]
# dc=[0,0,-1,1]
#
# # 초는 i+=1 같은 걸로. for문 하나 줄인. 녹일 수 있는 for문.
# # 모든 바이러스 1번확산 -> s초번해야.[while이든]<-> 인덱스 같이저장&sort& for in
# # for i in range(k):
# #    if len(biru[i]) > 0:  # i값, (ri,ci) # 1_(0,0)
#
# while (nbiru): # 1) while
#     val,t,r, c = nbiru.popleft() #2) deque_popleft()
#     if t==s:
#         break
#     for j in range(4): #3) 네 방향
#         nr=r+dr[j] # x랑 nr따로 있어야함. 이전 위치에서 각 네 방향으로 가야하니까.
#         nc=c+dc[j]
#         if 0 <= nr and nr < n and 0 <= nc and nc < n: # 4) ifif
#             if map0[nr][nc] == 0:
#                 map0[nr][nc] =val
#                 nbiru.append((val,t+1,nr,nc)) # 5) append
#
# print(map0[x-1][y-1])
# # 왜 바이러스 값도 저장했다가, 인덱스로 바꿨더라
# # > graph따라함_ 그 그래프는 연속적인 숫자라 빈 게 없어서 글케한거.
