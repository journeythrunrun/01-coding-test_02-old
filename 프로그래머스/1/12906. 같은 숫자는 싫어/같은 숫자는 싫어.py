# 원소 0~9
# 중복 제거 후 출력

# 같은 숫자는 싫어_https://school.programmers.co.kr/learn/courses/30/lessons/12906
# 나_(127.31ms, 27.9MB)
def solution(arr):
    # O(n) 너무 클듯_ 되네
    # m_ot)특수 정보 : 0~9숫자인 거 이용. 
    
    answer=[arr[0]]
    for a in range(len(arr)-1) :
        if arr[a]!=arr[a+1]:
            answer.append(arr[a+1])
    return answer

# 해설_같 (136.67ms, 27.9MB)
# def solution(s):
#     # 함수를 완성하세요
#     a = []
#     for i in s:
#         print(a[-1:])
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a


