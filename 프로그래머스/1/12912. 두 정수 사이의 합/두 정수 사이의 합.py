#두 정수 사이의 합_https://school.programmers.co.kr/learn/courses/30/lessons/12912?language=python3
def solution(a, b):
    # -7  4
    # 지금은 더 효율적인 수식 풀이보다, 조건 하에 빨리 풀고 피지컬 올리기.-> 걍 코드 스피드 좀 더 보고 더럽게 구현
    if a==b:
        return a
    answer=0
    # 부호가 다를 경우
    if a*b<0:#
        maxv,minv=max(abs(a),abs(b)),min(abs(a),abs(b))
        answer=sum(range(minv+1,maxv+1) ) #반대부호값 상쇄됨
        maxv,minv=max(a,b),min(a,b)
        if abs(minv)-abs(maxv) >0: #  7 - 4 = 3 # i) 양수_음수의 절댓값이 더 큼
            answer*=-1
        
    # 부호가 같을 경우
    else :
        maxv,minv=max(a,b),min(a,b)
        answer=sum(range(minv,maxv+1))
        #부호 함수
    
    return answer
    # # m_해설)
    # if a > b:
    #     a, b = b, a
    # return sum(range(a, b + 1)) # 이정도 시간복잡도도 괜찮았나보네    
