# 없는 숫자 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/86051
def solution(numbers):
    answer=0
    for i in range(10):
        if i not in numbers:
            answer+=i
    return answer
# 해설 : 효율화_수학적 m ((구현 속도용으로 풀어서 방법 생각 시도 아예 안함))
# : return 45 - sum(numbers)
    