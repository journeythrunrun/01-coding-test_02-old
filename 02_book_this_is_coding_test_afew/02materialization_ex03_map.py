# 1. 문제 : 게임 개발
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩

# 현재 위치 no에 방문표시 안했따.
# N, M=map(int, input().split())
# row,col,d = map(int, input().split())  # 위치, 시선
#
# map=[ [0]*M]*N #print([ [0]*M]*N) #g
# for i in range(N):
#     map[i] = map(int, input().split())  # 위치, 시선
#
#
# count, result=0,0
# no=[ [1]*M]*N #print([ [0]*M]*N) #g
# position=[col,row]
# move = [ [-1,0],[0,-1],[1,0],[0,1] ]
# new_posi=[0,0]
# while(1) :
#
#     if count==4 :# 뒤
#         k= 0 if d==3 else d
#         new_posi[1]= position[1]+move[k][1] ### [0,1] + [1,2] _ concatenate
#         new_posi[0]= position[0]+move[k][0] ### [0,1] + [1,2]
#
#         if map[new_posi[0]][new_posi[1]]==1 :# 뒤 칸이 바다
#             break
#
#         position+=move[k]#뒷걸음
#         # if d== 0:
#         #     position+=move[k]
#         # elif d==1:
#         #     x-=1
#         # elif d==2:
#         #     y-=1
#         # else :
#         #     x+=1
#
#     ## new_d
#
#     d_left=0 if d==3 else d-1 ## 왼쪽 turn
#     # 왼쪽방향의 no(미방문)들 더해서 체크하려했는데. 현재좌표(인덱싱),d 다 사용해야겠네
#     if sum( no[d_left]  ) > 0:  # 그쪽 방향이
#         d=d_left
#         position[1] += move[d][1]  ### [0,1] + [1,2] _ concatenate
#         position[0] += move[d][0]  ### [0,1] + [1,2]
#         result+=1
#         count=0
#         continue
#     count+=1
# print(result)

# - 해설
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)

# - 느낀점
# > 시간초과 _50m_생각을 코드로 구현 느림
# > 지문 ' 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 ' :
# >> 나 = 더 쉬운 의미랑 어려운 의미 중 엄밀히는 '내가 바라보는 방향의 모든 칸'이 맞다고 생각함
# >> 해설 = 보니까  '코앞 칸만 미방문'을 따지는 거였네. 저 no[]값 설정 및 단계 생각할 시간에 다른 거 했으면 더 나았겠다.
