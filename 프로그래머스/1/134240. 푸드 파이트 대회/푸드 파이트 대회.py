# 푸드 파이트 대회_https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 양쪽에서 음식 종류/양/순서 같아야/칼로리 낮부터
# food_칼로리 낮은순(물도이땅)_개수
# : 안 빔, 자연수, 

def solution(food): #[1, 3, 4, 6]
    # 구현속도용 풀이
    # : //2 -> a1 + '0' + a1[::-1]
    a=''
    for i in range(len(food)):
        a+=str(i)*( food[i]//2) # 반절(7_2로 나눈거)에서 사용개수(15->14_나머지1버려짐)
    return a+'0'+a[::-1]
        
# 해설 [시복 같]
# - 문자열을 중간부터 만들어나가는 부분이 흥미롭
# : answer = str(i) + answer + str(i)

# def solution(food):
#     answer ="0"
#     for i in range(len(food)-1, 0,-1):
#         c = int(food[i]/2)
#         while c>0:
#             answer = str(i) + answer + str(i)
#             c -= 1
#     return answer
    