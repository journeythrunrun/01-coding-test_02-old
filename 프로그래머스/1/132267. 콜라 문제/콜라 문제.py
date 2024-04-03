# 콜라 문제_https://school.programmers.co.kr/learn/courses/30/lessons/132267
# int(20/2) > # (넘 짧고 쉬워서 적으려다 그냥 바로 구현 들감)

# - 한글 주석으로 핵심 코드 의미 적어놔야, 더 엄밀 가능한듯. 놓치는 거 디버깅으로 발견하긴 하지만 ㅎㅋㅎ
# 통과 (0.48ms, 10.2MB) # 빈도는 0.01가
def solution(a, b, n):
    left=n
    answer=0
    # m_s) 굳이 반복?   등차등비(//a)*b  등 방법 있을 것 같
    # m) 걍 구현속도용풀이로해보자
    # n= a* k + a보다 작은 수 # k
    while(left >=a):
        answer+=(left//a)*b #k*
        left= left%a +(left//a)*b  # 남은거=먹고남은 거 + 새로 받은 거 
        
        # 음수시 몫 나머지는
    return answer

# 해설 [시복 비슷] # 굳이? 내 추가 시간소모 X
# solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

    