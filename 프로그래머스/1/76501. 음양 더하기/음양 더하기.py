# 음양 더하기_https://school.programmers.co.kr/learn/courses/30/lessons/76501

# - get
# np.sum / sum 시복_1차원에서 비슷. np가 worst가 심하고 평소엔 좀 더 좋음 
# np.int는 reutrn 불가

# import numpy as np
def solution(absolutes, signs):
    #m1) element wise_numpy만 암 
    # : 곱하는 놈들 같은데 연산도 더 효율인가. np부르는데 더 걸리나. <-> m2 for
    # [압축]_t 약 3배(시복은 비슷해서 그럴수도)_통과 (2.33ms, 28.4MB) 
    # return int( sum(np.array(absolutes)*(2*(np.array(signs) )-1) ) )


#     # [기본]_통과 (6.72ms, 28.3MB)
#     a=np.array(absolutes) # 복잡도_O(n)이라는데_시간은 더 걸릴 듯
#     b=2*(np.array(signs) )-1 # 0->-1 처리 (1->1)
#     # ax+b=y / b=-1 / a+b=1 -> a=2 / 2x-1=y 
#     return int( np.sum(a*b) ) # np.sum?
#     # int 안 씌우면 np.int64?32?형이라 return불가 _TypeError: Object of type int64 is 'not JSON serializable'
    
    
    #m2) for각각곱_차라리 빠름(m1_압축_np.sumd_worst 뺀 것보다 조금 더)_통과 (0.14ms, 28.3MB)
    answer=0
    for i in range(len(signs)):
        answer+=absolutes[i]*( True if signs[i]>0 else -1 ) # 0ㄱㅊ
    return answer
# 해설 
# : return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
# : > element-wise <=> zip
# : > 부호값으로 -를 곱하지 말고, 조건 만 따진 후 크기에다 '-'로 뒤집어
    