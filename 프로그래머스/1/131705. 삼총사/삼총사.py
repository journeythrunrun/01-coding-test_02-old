# 삼총사_https://school.programmers.co.kr/learn/courses/30/lessons/131705
# 합하면 0이되는 삼총사_경우의 수
# ( number = 안빔, 요소_'정수'&중복가능 )

#	통과 (0.13ms, 10.1MB)
def solution(number):
    # 3개고르는 경우의수_탐색 => sort하고 처리 효율적이겠다? 굳이 그렇게까지? 입력 길이도 짧다
    
    count=0
    comb=[]
    for i in range(len(number)-2  )  :
        for j in range( i+1, len(number)): # 뒤에서 자동으로 처리됨
            for k in range( j+1, len(number)):
                comb.append([number[i],number[j],number[k]])
    for i in range(len(comb)):
        count+=1 if sum( comb[i] )==0 else 0
    return count

# # 해설[비슷] 통과 (0.10ms, 10.1MB)
# def solution (number) :
#     from itertools import combinations
#     cnt = 0
#     for i in combinations(number,3) :
#         if sum(i) == 0 :
#             cnt += 1
#     return cnt
    

    