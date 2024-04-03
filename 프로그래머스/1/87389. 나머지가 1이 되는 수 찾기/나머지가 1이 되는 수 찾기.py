# 나머지가 1이 되는 수 찾기_https://school.programmers.co.kr/learn/courses/30/lessons/87389
def solution(n):
    answer = 0
    for i in range(1, n + 1):
        if n % i == 1:
            answer = i
            break

    return answer