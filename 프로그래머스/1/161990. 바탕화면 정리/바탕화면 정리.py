# wallpaper	result
# [".#...", 
#  "..#..", 
#  "...#."]	[0, 1, 3, 4]

# 1)
# 정사각형 / 왼위(0세로_행,0가로) / 값_ 빈칸("."), 파일유("#")

# ->[ 모두 지우는, 최소한의 이동거리 => 시작점(작은 거), 끝점]
# 드래그 한 거리 : 가로차 세로차 | rdx - lux| + |rdy - luy |

# 2) 양쪽 max
# : 최소 행인덱스, 열인덱스 / 최대 행인덱스 열인덱스
def solution(wallpaper):
    answer = []
    minr=len(wallpaper)-1 
    minc=len(wallpaper[0])-1
    maxr = maxc=0# 

    for i, row in enumerate(wallpaper):
        for j, a in enumerate(row):
            if a=='.':
                continue
            else : # '#'
                # print('max',maxr, maxc )
                minr=min(minr, i)
                minc=min(minc, j)
                maxr=max(maxr,i)
                maxc=max(maxc,j)
                # print('max_2',maxr, maxc )
                # print(i,j)
        
    answer=[minr,minc,maxr+1,maxc+1]
    # m2 간략화_ 루프 돌면서 업데이트된 min max범위 밖만 체크할 수도 있겠다.                
    return answer
# : 20m / 성능 +2 / 최대 0.99ms
# -> (엄청 금방 푼 느낌이었는데, 생각보다 문제 읽는 게 시간 걸리나봄)

# - 디버깅 : 격자가 정사각형, 바탕화면 자체는 정사각형X    
# > 결과<->정답 비교 및 특징추출 = 일단+1 함->정답
# : 이유_ 파일이 좌표위에 있는 게 아니라, 좌표 사이에 있음 / 그래서 왼쪽위는 인덱스지만 오른쪽 아래는 인덱스+1씩임

# - 다른 사람 코드
# > 일단 #append 하고 한번에 거기서min, max찾기.
    #         if wall[i][j] == "#":
    #             a.append(i)
    #             b.append(j)
    # return [min(a), min(b), max(a) + 1, max(b) + 1]
# [1] 요서비 , 김래현 , 신제우 , dlwldnjs1009@gmail.com 외 95 