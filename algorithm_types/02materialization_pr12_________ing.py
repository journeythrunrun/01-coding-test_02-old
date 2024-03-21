def solution(n, build_frame):
    map = [[0] * (n + 1) for _ in range(n + 1)]

    for act in build_frame:
        x, y = act[0], act[1]

        if act[3] == 0:  # 삭제_ 삭제 실행>조건체크>다시건축
            if act[2] == 0:  # 기둥
                if (map[x][y + 1]) == 0:
                    if map[x - 1][y + 1] == 1 or map[x][y + 1] == 1:
                        pass
                    else:
                        continue
                elif map[x][y + 1] == 1:
                    if map[x][y + 1] == 1 and map[x + 1][y + 1] == 1:
                        pass
                    else:
                        continue
                # $ 삭제 실행
                map[x, y] = 1

            elif act[2] == 1:  # 보 삭제
                # $
                map[x, y] = 0

        elif act[3] == 1:  # 설치
            if act[2] == 0:  # 기둥
                if y == 0 or map[x - 1][y] == 1 or map[x][y] == 1:  ##dx
                    pass
                elif map[x][y - 1] == 0:
                    pass
                else:  # 설치 못함
                    continue
                # 설치 실행
                map[x][y] = 0
            elif act[2] == 1:  # 보
                if map[x][y] == 0 or map[x + 1][y] == 0:
                    pass
                elif map[x][y] == 1 and map[x + 1][y] == 1:
                    pass
                else:
                    continue
                # 설치실행
                map[x][y] = 1

    answer = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            # target=map[i][j]
            if map[i][j] == 0:
                answer.append([i, j, map[i][j]])

            elif map[i][j] == 1:
                answer.append([i, j, map[i][j]])

    answer.sort()

    # 교차점 반환
    return answer




















def solution(n, build_frame):
    map = [[-1] * (n + 1) for _ in range(n + 1)]

    for act in build_frame:
        x, y = act[0], act[1]
        if act[3] == 0:  # 삭제_ 삭제 실행>조건체크>다시건축
            if act[2] == 0:  # 기둥
                if (map[x][y + 1]) == 0:
                    if map[x - 1][y + 1] == 1 or map[x][y + 1] == 1:
                        pass
                    else:
                        continue
                elif map[x][y + 1] == 1:
                    if map[x][y + 1] == 1 and map[x + 1][y + 1] == 1:
                        pass
                    else:
                        continue
                # $ 삭제 실행
                map[x, y] = 1

            elif act[2] == 1:  # 보 삭제
                # $
                map[x, y] = 0

        elif act[3] == 1:  # 설치
            if act[2] == 0:  # 기둥
                if y == 0 or map[x - 1][y] == 1 or map[x][y] == 1:  ##dx
                    pass
                elif map[x][y - 1] == 0:
                    pass
                else:  # 설치 못함
                    continue
                # 설치 실행
                map[x][y] = 0
            elif act[2] == 1:  # 보
                if map[x][y] == 0 or map[x + 1][y] == 0:
                    pass
                elif map[x][y] == 1 and map[x + 1][y] == 1:
                    pass
                else:
                    continue
                # 설치실행
                map[x][y] = 1

    answer = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            # target=map[i][j]
            if map[i][j] == 0:
                answer.append([i, j, map[i][j]])

            elif map[i][j] == 1:
                answer.append([i, j, map[i][j]])

    answer.sort()

    # 교차점 반환
    return answer

print(solution())
