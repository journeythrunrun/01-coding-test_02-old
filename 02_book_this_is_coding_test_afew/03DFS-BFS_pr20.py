# 20번_https://www.acmicpc.net/problem/18428
# - 나
# : 혼자_1h 20m (제한시간 1h)
# : 종이에 풀이 순서만 쓰고, 알고리즘 안씀 -> 생각을 구현이 걸렸네 & 쓰면서 구체화
# - 주의 사항
# : "반복문, 회귀문 속에서의 '자료형'변수의 변화 _특히 pop"
# : 변수 내용'이 원하는 대로 나오는지 각각 확인.
# <-> 해설 itertools.combinations_((튜플 속 튜플)?, ) , copy미사용
# : ((0, 0), (0, 2), (0, 3))  #  리스트 입력도 받음-> 튜플 반환

import copy
n=int(input())
map0=[]
teac=[]
noth=[]
for i in range(n):
    map0.append(list(map(str,input().split()))  )
    for j in range(n):
        if map0[i][j] == 'T':
            teac.append([i,j])
        elif map0[i][j]=='X':
            noth.append([i,j])
# C _index
leng=len(noth)
index_x=[]
for i in range(leng):
    for j in range(i+1,leng):
        for k in range( j+1, leng):
            index_x.append([i,j,k])

dr=[0,0,1,-1] # 동서 남북
dc=[1,-1,0,0]
def check_T(now):
    # (해설_good)for _ in teac  <-> (나) 복사&while&pop
    while (teac2): # teac는 deepcopy아니라, 이전 반복에서 사용하고 이미 비었음
        r,c=tuple(teac2.pop())#[3,5]
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            while( nr < n and nr > -1 and nc <n and nc >-1 ):
                if map2[nr][nc]=='S':
                    return False
                elif map2[nr][nc]=='O':
                    break
                nr+=dr[i]
                nc+=dc[i]
    return True
now = False
for inde in index_x:
    i,j,k=inde[0],inde[1],inde[2]

    # copy <->(해설)3개만 바꾸니까 값 줬다 뺐는 게 낫다.(전염아니라)
    map2=copy.deepcopy(map0)
    teac2=copy.deepcopy(teac)
    map2[noth[i][0]][noth[i][1]]='O'
    map2[noth[j][0]][noth[j][1]] = 'O'
    map2[noth[k][0]][noth[k][1]] = 'O'

    now=now or check_T(now)
    # '한 번이라도 되면' YES
    if now == True:
        break
if now==True :
    print("YES")
else :
    print("NO")


# - 해설
from itertools import combinations

n = int(input()) # 복도의 크기
board = [] # 복도 정보 (N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))

# 특정 방향으로 감시를 진행 (학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장애물들을 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')
