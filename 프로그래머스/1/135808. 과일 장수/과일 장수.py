# 과일 장수_https://school.programmers.co.kr/learn/courses/30/lessons/135808
# 사과 [1,k]점_ m개
# 박스 가격 = 가장 낮은 점수 * m개
# 가능한 많은 사과를 팔 수 있을 때, ㄱㄴ 최대 이익
# *이익 미발생 =0, max(0, result)

# - !문제 암기, 필기 놓침_여러 상자 팔 수 있음
def solution(k, m, score):
    # 여러 상자=비싼놈들끼리 하는게낫다. 최저점이 어차피 하향평준화라.
    # 최고 점수부터 > 그중 가장 최저점수min
    score.sort()     
    # -파라미터 안쓰이기도. k가 안 쓰이긴 하네
    
    # # m2) [시간비슷]통과 (92.71ms, 21.6MB) 
    # i=m
    # result=0 # comprehension과 sum으로 압축할 수 있는데 그건 시복 좀 더 생기는 건 아닌데(O(1)연산등이라).연결연산이긴해서. 이건 메모리 추가 버리는 거 같긴 했는데 걍 다 비슷
    # while(i <= len(score) ): # 뒤에서 i번째라 그냥 인덱스 아님. # 뒤에서 n개수 번째까지 ㄱㅊ
    #     result+=score[-i]*m # ! 점수 "*개수"
    #     i+=m
    # return max(0,result)

    # m1) (100.05ms, 21.6MB)    
    return max(0,sum([score[-i*m-m]*m for i in range(len(score)//m) ])) # m개 # 

# - 해설_[유사]_내께 낫다 (110.04ms, 26.1MB)
# : 나_for 대신 해설_slicing  : 그걸 n~ 만큼 해서 시간 비슷
    # return sum(sorted(score)[len(score)%m::m])*m