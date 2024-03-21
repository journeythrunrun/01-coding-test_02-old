# 미로 탈출


# 나는 스택에 한거보니 dfs와 비교해야할듯

# '최단'거리 ==bfs_큐에서 bfs계산하면서, 자동으로 '최단'count'갱신'?  / not dfs.()
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 소스코드 구현
def bfs(x, y):
    # 큐사용
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()  # 큐니까 삽입/삭제 중 하나는 left
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue

            # 맵 내 & 맵 값1
            if graph[nx][ny] == 1:  # 최단 거리 저장하고 있어서, 1이면 처음 방문한 거임.
                graph[nx][ny] = graph[x][y] + 1 # 현재 pop한 대상의 근처니까.
                queue.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0, 0))

# # 나)
# # 행열(r,c)로_어차피 입력이 행열로 들와, 자료 구조에도 그 모양 그대로.
#
# n, m = map(int, input().split())
#
# visited = [[n * m + 1] * m for _ in range(n)]
# alread = [[0] * m for _ in range(n)]
#
# map = []
# for _ in range(n):
#     map.append(list(map(int, input())))
#
# count = 0
#
#
# def go(r, c):
#     if r < 0 or r >= n or c < 0 or c >= m:
#         retun
#         False  # ?
#     if map[r][c] == 0 or alread[r][c] == True:
#         return False
#     # map이 1값 & 방문한 적 없
#     # 방문했던지
#     count += 1
#     if count < visit[r][c]:
#         visit[r][c] = count
#     if r == n - 1 and c == m - 1:  # 도착
#         return True
#
#     return True
#
#     go(r, c + 1)  # 동
#     go(r + 1, c)  # 남
#     go(r, c - 1)
#     go(r - 1, c)
#
#     return True  # ?
#
#
# start_in = [0, 0]
# result = 0
# go(start_in[0], start_in[1])
# print(visit[r][c])
#
#
