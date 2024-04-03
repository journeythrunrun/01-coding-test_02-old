# 평균 구하기_https://school.programmers.co.kr/learn/courses/30/lessons/12944
def solution(arr):
    answer = 0
    for a in arr:
        answer+=a
    answer/=len(arr)
    return answer