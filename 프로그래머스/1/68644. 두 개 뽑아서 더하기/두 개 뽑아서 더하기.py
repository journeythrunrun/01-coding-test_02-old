# 두 개 뽑아서 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    # m1) 라이브러리_구현이랑 t비슷. 걍편리함.) 통과 (4.84ms, 10MB) 
    from itertools import combinations
    answer=[]
    for a,b in combinations(numbers,2) :
        if a+b not in answer :
            answer.append(a+b)
    # m2) 통과 (4.93ms, 10.1MB)
#     answer=[]
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] + numbers[j] not in answer :
#                 answer.append(numbers[i] + numbers[j])    
    
    answer.sort()
    return answer

# 해설 [비슷]
# - 나_중복 제거용 조건문 => set 씌워
# - 조합 = 예전 내가 생각해낸거((당연한거긴한데 이렇게 흔하게 있는 거였다늬. 그래도 set도 있긴해도 추천 많이 받은 코드에 있는 거니 의민 있겄지))

# def solution(numbers): # 	통과 (0.53ms, 10.1MB)
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])    
#     return sorted(list(set(answer)))
