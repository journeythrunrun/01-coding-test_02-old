# 0 덩어리
n,m=map(int, input().split())
map0=[]
for _ in range(n):
    map0.append(list(map(int, input())))# 1234 -> 1 2 3 4 : map만. .split('')같이 쓰면 안됨.

dr=[0,0,1,-1]
dc=[1,-1,0,0]
result=[0]
def bfs(v): # 한덩어리씩 count하는놈
    if map0[v[0]][v[1]]==0 :#~
        return False
        for i in range(4):# 0인놈들 0화
            newr=v[0]+dr[i]
            newc=v[1]+dc[i]
            if bfs([newr,newc],) :



bfs([0, 0])
print(result[0])


n,m=map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #0 -> 이미 센 거 1화(없다칠거라 걍 치환하듯 그렇게해준거) & 네방향0탐색해서 1화
    if graph[x][y]==0: #
        graph[x][y]=1 # 방문처리를 가진 값을 1로바꿔버리네 ?
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True # count한다잉
    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1
print(result)

# me_ㅠ)
# n, m = map(int, input().split())
# lines = []
#
# for i in range(n):
#     lines.append( list(map(int, input()) ))#map이 병렬화 하는듯
#
#
# result = 0
# count_visited = [[0] * m for _ in range(n)]
# for i in range(n):
#
#     for j in range(m):
#         temp = []
#         try:
#             temp.append(count_visited[i + 1][j])
#         except:
#             pass
#         else :
#             temp.append(count_visited[i + 1][j])
#
#         try:
#             temp.append(count_visited[i - 1][j])
#         except:
#             pass
#         else :
#             temp.append(count_visited[i - 1][j])
#
#         try:
#             temp.append(count_visited[i][j + 1])
#         except:
#             pass
#         else :
#             temp.append(count_visited[i][j + 1])
#
#         try:
#             temp.append(count_visited[i][j - 1])
#         except:
#             pass
#         else:
#             temp.append(count_visited[i][j - 1])
#
#         if lines[i][j] == 0: #count_visited[i][j] == 0 and_ 어차피 non visit
#             result += 1
#             count_visited[i][j] = 1
#         # 주변에 이미 visited있었으면 다시 빼기 1
#         if lines[i][j] == 0 and sum(temp) > 0:
#             result -= 1
#         print(i,j,result)
# print(result)

# me_ㅠ) 내 코드 :이전0모임과 현재보는 것의 아래에서 연결되는 경우도(순서대로탐색이라 아직 연결성 표현 못한 부분) count해버림 -> 0 => 주변0 모두 미리 처리하는 식으로
# sol) 마인드맵 처럼 확장적 -> 재귀함수 [스택,..]
