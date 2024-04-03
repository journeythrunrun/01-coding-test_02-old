# 내적_https://school.programmers.co.kr/learn/courses/30/lessons/70128

# 내적 
# 음수,0 있음
# ( 길이 같, 안 빔 )
def solution(a, b):
    return sum( [i*j for i,j in zip(a,b)] ) 
# 해설_같