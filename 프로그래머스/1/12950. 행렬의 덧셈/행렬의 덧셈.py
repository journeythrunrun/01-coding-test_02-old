# 행렬의 덧셈_https://school.programmers.co.kr/learn/courses/30/lessons/12950
# -wise

def solution(arr1, arr2):
    # [1,2] [3,4]
    # [ 제거] [ [ 0]*n for _ in range(n)]
    return[[a+b for a,b in zip(row1, row2) ] for row1, row2 in zip(arr1, arr2) ]
    
# 해설[같음]
# return [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]