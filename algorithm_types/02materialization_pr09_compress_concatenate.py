# 1. 문제 : 문자열 압축
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
# def solution(s):
#     inpu = list(input())
#     result = []
#     answer = 0
#     n_max = len(inpu) // 2
#     for n in range(2, copy + 1):  # inpu에서 n개씩 검사
#         i, count = 0, 0
#         if len(inpu) % n != 0:
#             continue
#         # 검사
#         seta = set()
#         while (1):
#             old = inpu[i:i + n]
#             present = inpu[i + n:i + 2n]
#             if (present == old):  # 앞이랑 같으면
#                 count += 1
#             else:  # 이전것과 다르면_ update
#                 k =
#                 result.append(k)
#             i += n
#             if i + 2n > len(inpu):
#                 break
#     return answer

# - 해설. 주석 : ##나
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step): #비교라서 이건 두번째것 부터라 step이 시작., <-> 나는 while(1) & j초기화 &j+=step
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev ## 문자열+리스트 concatenate 연속기
                prev = s[j:j + step] # 다시 상태 초기화 ## < 이전 것과 비교 >_1)초기값_[0],2) for_[1],len,step 3) 이전값도 업데이트
                count = 1

        # 남아있는 문자열에 대해서 처리 ## 이전것과 비교하는 알고리즘에서, 마지막 꺼를 조건문 밖에서 처리.
        compressed += str(count) + prev if count >= 2 else prev  ## 마지막 것 : if_앞 것과 같을 때 else_다를 때
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed)) ## 최소값 = 비교 조건문 -> min(, )
    return answer

# - 시간초과
# > 코드화 느림 : 알고리즘은 많이 비슷한데, 코드화에 익숙하지 않아서 아직 많이 느림
# -> 정답_좋은 코드 보고, 코딩작성연습 해나가면서 자연스레 늘어갈 요소
# - 느낀점
# > 전부 손코딩은 오래 걸림 -> 핵심, 조건문 설계, 변수 정도
# > ## 주석


