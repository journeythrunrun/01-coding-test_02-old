# x: 양의정수
# 각 자릿수 합  으로 x를 나눴을 떄 나머지 0
    
def solution(x):
    #answer = True
    a=0
    for i in str(x) :  #"10"
        a+=int(i)
    if x%a ==0:
        answer=True
    else:
        answer=False
    # 해설m) sum(int(x) for x in str(n))  # generator의 sum ㄱㄴ
    
    return answer