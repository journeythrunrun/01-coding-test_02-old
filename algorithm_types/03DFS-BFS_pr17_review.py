# - 다음날 복습
# : 30m
from collections import deque

n,k= map(int, input().split())
# - 리스트_차이
# list(  ) : 괄호 안 변수의 가장 바깥 형식을, list형식으로 바꿈
# [  ] : list 안에 담음
map0=[]
viru_all=[] # [ [v_value, r,c, t] ,[1, , , 0], [2,
for i in range(n):
    map0.append(list(map(int, input().split()) ))
    for j in range(n):
        if map0[i][j] != 0:
            viru_all.append([map0[i][j],i,j,0])
viru_all.sort()
s,x,y= map(int, input().split())

# bfs

dr=[0,0,1,-1]
dc=[1,-1,0,0]

node_using=deque(viru_all) # 탐색 대상. 큐? 디큐? 두가지 아니었나 /정렬된거랑/큐랑
while(node_using):
    v=node_using.popleft() # [v_value, r,c, t] # 이미 값있는 위치

    if v[3]==s:
        break
    # 네 방향
    for i in range(4):
        nr=v[1]+dr[i] # dr'[i]' 또 빼먹네
        nc=v[2]+dc[i] # 새 탐색 대상
        if nr <n and nr >-1 and nc<n and nc >-1 :
            if map0[nr][nc]==0:
                map0[nr][nc]=v[0]
                node_using.append([v[0],nr,nc,v[3]+1])

print(map0[x-1][y-1])


