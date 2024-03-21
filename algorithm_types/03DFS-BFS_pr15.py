#
# 해설 : '최단' 거리 & 간선 비용 동일 -> BFS
# 두번째 자료구조에 최소 거리정보 저장(+1씩)
from collections import deque
n, m, k, x = map(int, input().split())
# 그래프(_m2인접리스트) 자료구조로 표현
graph = [[] for _ in range(n+1)]  # 0인덱스 안씀
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # inpu.append( list(map(int, input().split())) )


distance=[-1]*(n+1)
distance[x]=0 # 출발 도시까지의 거리는 0으로 초기화

# bfs라서 자동으로 최소거리값. 방문
q=deque([x])
while q:
    now=q.popleft()
    for next_node in graph[now]:
            # 미방문
        if distance[next_node]== -1: # (( bfs나중 께 min일 수는 없으니까 최초 거리로 ))
            # count대신_ 이전 최소값에서 1씩 더해주네
            distance[next_node]=distance[now]+1
            q.append(next_node)
check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)
# 나 2
# ### distance 써라아아
# # 나 2차(며칠 후)_40m
# n,m,k,x=map(int, input().split()) # 도시 수, 도로 수, 거리정보, 출발도시
#
# answer=[]
# from collections import deque
# road=[[] for _ in range(n+1) ]
# for _ in range(m): # 1 2, 1 3, 2 3,
#     a,b=map(int,input().split())
#     if b<a:
#         a,b=b,a
#     road[a].append(b)
# # sort 안 해도 괜찮을 조건 없으니 해야할 것 같은데/ 해설도 안하고 시간 초과돼버리니 pass
# for i in range(n):
#     road[i+1].sort()
# # bfs
#
#
#
# visited=[False]*(n+1)
# queue=deque()
# queue.append(x)
# visited[x]=True #1
# count=0
# c=[1]#
# j=0
# while queue: #
#     x = queue.popleft() #1 /2pop
#     c[j]-=1 # c[0]=0 # 남은 것중 가장 먼저 위계의 count감소
#     ## X_temp_count -=1
#     ## (k=1인거) k=1인 동일 위계 노드들이 삭제될 때만 temp_count가 감소하긴함
#     ##  근데 동일 위계 temp_count = 숫자가 0으로 감소 되기전에, 다른 위계에서 temp_count가 증가해버림
#     ## > temp count를 인덱스에 저장하던가..
#
#     #X '삭제'나 '삽입'만 보면, 최소 거리 순이 맞음.
#     #X '시간'으로 보면 코드상에서 pop(temp_count -)과 삽입(temp_count +)가 겹쳐섞임.
#
#     #~#~#~#~#~#~#~#~#~#~# 여기이~
#     # -> count가 for 밖에서 같진 않어 [_for_ [1]2_for / [1]3_for  ]
#     # -> 아니근데 탐색순서도 bfs인데
#     # -->k 횟수를 '탐색'을 기준으로 했으면, 'pop' 기준으로 count세면 안되지?
#     if c[j]==0:
#         count += 1 # 아래 for문 애들이 가지는 count
#         ### 2와 3의 다음놈들이 같은 걸 못가지는 것 같음.
#         j += 1
#     # count 1, temp_count 0
#     temp_count = 0
#     for i in road[x]: # i_2  ,   3
#         if visited[i]==True:
#             continue
#         queue.append(i) # 2
#         visited[i]=True
#         # k나오면 줄일 수 있
#         if count == k:  ## k ### pop기준으로 count 조건생각한거같음
#             answer.append(i)
#             print('suc', i, c, c[j]  )
#         temp_count+=1
#
#         print(count, i)
#         print (c)
#
#     c.append(temp_count)
#
#
# answer.sort() #자동으로 낮은 숫자부터?는 아닐듯. 2->7, 3->5 일 수 있
# if len(answer)<1:
#     print(-1)
# else :
#     for j in answer:
#         print(j)
#

#
# # 나
# n, m, k, x = map(int, input().split())
# # 그래프(_m2인접리스트) 자료구조로 표현
# graph = [[] for _ in range(n+1)]  # 0인덱스 안씀
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     # inpu.append( list(map(int, input().split()))  )
#
# result = []
# count = 0
# graph2=[ 300000 for _ in range(n+1)]
#
# ##dfs->bfs : 최소값 체크
# # count 초기화
# def dfs(graph, v, k, count):
#     for i in graph[v]:  # 2,3
#         count += 1  # 2,3
#         if count<graph2[i] and graph2[i]!=0:
#             graph2[i]=count # 최소저장  # 도시   ##[i,]
#         dfs(graph, i, k, count)
#         ##### 그때 미방문 체크했던 이유는
#         # -> 똑같은 노드들 서로 화살표로 왔다갔다 방지[스택으로 자동 선] ? 중복값 처리는
#
#     count -= 1  ## 함수 종료가 pop이니 빼주면
#     return True
#
#
# # visit_X_이번엔 방향있어서? 방향있어도 무한에 갇힐 수 있지 않나나
# from collections import deque
# def bfs(graph,x):
#     queue=deque([x])
#     #
#     while queue:
#         v = queue.popleft()
#
#         for i in graph[v]:
#             queue.append(i)
#
# bfs(graph, x)
#
# j=0
# for i in graph2:
#     if i==k:
#         result.append(j)
#     j+=1
# if len(result) == 0:
#     print(-1)
# else :
#     result.sort()
#     for i in result:
#         print(i)