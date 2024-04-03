# 폰켓몬_https://school.programmers.co.kr/learn/courses/30/lessons/1845
# N/2 가져도 된대_ 최대한 많은 종류의 개수
# 안빔_ , 자연수

def solution(nums):
    a=set(nums) # 몇 종류 있니 # 7개
    max_get=len(nums)/2 # 6개 #N/2
    return min(len(a), max_get)
# 해설 똑같
    