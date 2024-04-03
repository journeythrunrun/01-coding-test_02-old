# 짝수와 홀수_https://school.programmers.co.kr/learn/courses/30/lessons/12937
def solution(num):
    answer = ''

    if num % 2 == 0:
        # answer="Even"
        answer = answer.join('Even')
    else:
        # answer="Odd"
        answer = answer.join('Odd')

    return answer