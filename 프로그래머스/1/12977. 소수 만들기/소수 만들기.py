# 소수 만들기_https://school.programmers.co.kr/learn/courses/30/lessons/12977
# 3개의 수를 더했을 때 소수가 되면 count
# 안빔, 자연수. 중복 없음

# 통과 (46.44ms, 11.1MB)_worst t
def solution(nums):
    from itertools import combinations
    a=list(combinations(nums,3)) # [ (1,2,3), ]
    print(a[0][0])
    count=0
    for i in range(len(a)):
        target=sum(a[i]) # 9
        
        # 소수 체크 7 = 1*7 // sqrt(자신)까지 나눠보기
        j=2
        real=True
        
        while(j<=target**0.5): # 경계값 j=3 # +1,2아니고 유무라 경계값 처리 위치에 따라 연산해야하는 게 달라지진 않음 # 경계값 포함.
            if target%j==0:
                real=False
                break
            j+=1
        if real==True:
            count+=1
    return count

# 해설[ 내께 시복 더 낫다]
# - 메모리 아낌_ a in combinations(nums, 3):
# - 코드 단축_for/while&break + else :: True False 변수 생략 ㄱㄴ

    
    