# 자릿수 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/12931
def solution(n):
    answer = 0

    nn=str(n)# "123"
    for i in nn:
        answer+=int(i)
    return answer