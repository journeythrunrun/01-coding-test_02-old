# 1. 문제 : 자물쇠, 열쇠로 열기
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
# def solution(key, lock):
#     # lista=[[1,2],3]
#     # # print(len(lista)) #2
#     # for i in lista :
#     #     print(i)
#
#     ## len ->index
#     # 자물쇠에서 충족해야할 target 부분 찾기 [key가 벗어나도 되는거 해결관련]
#     minx, miny, maxx, maxy = 0, 0, 0, 0
#     answer = false
#
#     for i in len(lock):  # ##for i in lock:
#         for j in len(lock[i]):
#             if lock[i][j] == 0:
#                 minx = min(minx, i)
#                 miny = min(miny, j)
#                 maxx = max(maxx, i)
#                 maxy = min(maxy, j)
#     # target
#     target = lock[minx:maxx + 1][miny:maxy + 1]
#     ## 0인값을 1로 1인값을 0으로 #(value-1)*(-1) _element-wise 연산
#
#     # 2) 가능한 키 들
#     target_n = (maxx + 1 - minx) * (maxy + 1 - miny)  # 몇칸으로 맞춰야하는지
#
#     stepx, stepy = len(target), len(target[0])  # 2,2
#
#     # 이동
#     for in key[]:
#         i = 0
#     while (1):
#         j = 0
#         while (1):
#             j += 1
#             ##회전 추가해야
#             if key[i:i + stepx][j:j + stepy] == target
#                 answer = True
#
#             # for 대신종류구문
#
#         i += 1
#         # ''
#     return answer


# - 해설, 내주석 : ##

# 2차원 리스트 90도 회전하기
def rotate_a_matrix_by_90_degree(a):
    n=len(a) # 행 길이 계산
    m=len(a[0]) # 열 길이 계산
    result=[[0]*n for _ in range(m)] # 결과 리스트
    for i in range(n) :
        for j in range(m):
            result[j][n-i-1]=a[i][j]
    return result
# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length=len(new_lock) //3 ## 탐색 대상을 위해 *3을 해줬었지만, 맞춰야하는 곳은 *3 이전이니
    for i in range(lock_length, lock_length*2): ## 원래 자물쇠를 *3 한 거에서 가운데에 위치 시켰기에
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] !=1:
                return False
    return True

def solution(key, lock):
    n=len(lock)
    m=len(key)
    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock=[i+n][j+n]=lock[i][j]
    # 4가지 방향에 대해서 확인
    for rotation in range(4):
        key=rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for x in range(n*2): ## for 4개 : x,y_탐색 대상 위치 / i,j_열쇠 모양에 맞는지
            for y in range(n*2):
                # 자물쇠에 열쇠를 끼워 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j] ## 더하면 1이 되는지 볼거라 <->나 ; 0,1 뒤집식&행열일치
                # 새로운 자물쇠에 열쇠가 정확히 들어 맞는지 검사
                if check(new_lock)==True:
                    return True
                # 자물쇠에서 열쇠를 다시 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
    return False
# - 시간초과
# > 반복문, 구체화 느림

# - 느낀점
# > 제한 시간 안에 rotate문제까지 해야됐던 거면, 암기든 뭐든 카카오 능숙 수준 요구구
