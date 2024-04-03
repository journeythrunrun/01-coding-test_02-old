# 명예의 전당 (1)_https://school.programmers.co.kr/learn/courses/30/lessons/138477

# 매일 점수 -> k 번쨰 이내 = 목록올림 (k 번쨰놈보다 크면) -> 최하위점수
# : 제한
# k=자연수
# score=안빔, 0이상, !중복 ㄱㅊ

# - 쉬운데 괜히 sort같은 거 안쓰려다 시간 더 걸림(오히려 예쌍과 다르게 쓰는것도 ㄱㅊ했기도) -> 시복 비슷하면 그냥 구현속도용 방법으로 ㄱㄱ
# - 생성한_배열 길이!!생각 
def solution(k, score):# 통과 (1.09ms, 10.3MB)

    # 상위3개중 min값
    result=[]
    topv=[]
    for i in score: # 10, 100, 20
        if len(topv)<=k-1 :#~! 2-> 결과로 3됨 ### 아침 꽉 안찬상태일때! pop쓸때! 길이주의
            topv.append(i)
        elif i > topv[-1] : # 랭킹화 # 'minv'와의 중복은 무시가능.
            topv.pop() # 젤 작은놈제거 ## 중복가능하니 한개만 ## 인덱스주의
            topv.append(i) 
        topv.sort(reverse=True)
            
             # 단순 minmin아냐. 300나오면 어쩌려구 # topv필요할듯. 값 업데이트 하다보면 나중에 비교할 일 생겨서결국.
            
        result.append(topv[-1]) #
    return result

# 해설 
# - 근데 해설법 remove중첩min 이 시복 더 큰거같기도 nn
# - 해설_간단_"remove(min)" <-> 나 sort&pop&[-1]
# .remove(min(q))

    
    