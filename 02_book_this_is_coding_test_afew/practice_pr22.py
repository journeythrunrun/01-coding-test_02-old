# pr22_https://school.programmers.co.kr/learn/courses/30/lessons/60063
# 최소시간 / 90도 회전
# bfs
# 최소시간 dfs

# 방문하지 않은 모든 0 칸 가기.
#

# 무조건 갈 수 있는 거만 준다고 했으니, 회전한 위치 까지는 몰라도 되겠다.
# 0 길찾고
# 가려는 방향에서 두값 0인지 비교 [a:a+2] / 회전숫자 업하고 비교
dr = [0, 0, 1, -1, 1, 1, -1, -1]  # 오른 쪽 기준 8가지 방향
dc = [1, -1, 0, 0, 1, -1, 1, -1]  # 리스트라서 다른 함수 끼리도 쓸수 있는 거 아니었나..


def dfs(v, distance, board):
    distance += 1  # ~최소값 재귀함수속 전달 / 예전파이참 문제 훑
    # 함수 탈출하면서 distance자동으로 1 빠지려나

    if v[0] == len(board) - 1 and v[1] == len(board[0]) - 1:
        return 1  # 재귀 속이어도 동일한 return값으로 계속 탈출# while...

    # 이미 왼쪽이 0이라 오른쪽발 기준으로 주변이 0이면 다 갈 수 있으니, 탐색.
    for i in range(8):
        newr = v[0] + dr[i]
        newc = v[1] + dc[i]

        if newr > -1 and newr < len(board) and newc > -1 and newc < len(board[0]):
            if board[newr][newc] == 0:
                if newr == len(board) - 1 and newc == len(board[0]) - 1:
                    answer[0] = min(answer[0], distance)  # ~+1? 함수 바로 아래 조건문에 해버리면 탈출때 귀찮아질 수잇음?
                board[newr][newc] = 1  # ~ 저번 코드들 파이참 보자
                dfs([newr, newc], distance, board)

    return 0


answer = [1000000]


def solution(board):
    # visited=[[False]*len(board[0]) for _ in range(len(board)) ]
    board[0][0], board[0][1] = 1, 1  # True, True
    # ㅇ
    dfs([0, 1], -1, board)  # ~첨에 1더해주는것땜시 # 보드 안 넣으면 정의 안됐다고 뜨네
    return answer[0]

# 40분 _틀렸음_디버깅보다 복습하고 오는것도.


# 이것이 코딩테스트다 _ 난이도 3 _ 50분