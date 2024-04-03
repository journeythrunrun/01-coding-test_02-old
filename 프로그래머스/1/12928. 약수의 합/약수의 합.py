# 약수의 합_https://school.programmers.co.kr/learn/courses/30/lessons/12928
# [약수] 1) 나눌 초기값1 2) 제곱근 케이스, 따로 1개만 더해
def solution(n):
    answer = 0
    k=1 # 약수를 위해 나눠볼 변수_초기값 1
    if n==0:
        return 0
    while( k<n**0.5):
        if n%k==0:
            answer+= k+n//k
        k+=1
    if k==n**0.5:
        answer+=k
    return answer