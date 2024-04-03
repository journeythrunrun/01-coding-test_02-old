# 예산_https://school.programmers.co.kr/learn/courses/30/lessons/12982
# 최대 몇 개의 부서에 ㄱㄴ
# ( d = 안빔 , 요소_자연수 / budget = 자연수 )

# (0.04ms, 10.1MB)
def solution(d, budget):
    d.sort(reverse=True)
    count=0
    while(len(d)): 
        budget-=d.pop() # pop=길이 체크하기_미리 몰랐다.
        if budget >=0:
            count+=1
        else :
            break
    return count

# 해설 [ 효율성 안좋아보임 ]
# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)
    