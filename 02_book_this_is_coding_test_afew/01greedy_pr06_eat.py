# 1. 문제 : 무지의 먹방 라이브
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
# def solution(food_times, k):
#     left_index = list(range(1, len() + 1))
#     answer = 0  # index_inde
#     # kk = 1
#     if sum(food_times) <= k:
#         return -1
#     while (1):  # kk < 2000000):
#         ### 리스트 비었으면 break
#         #       if
#         # 섭취할 음식 없으면
#
#         # min 시간복잡도 절약?
#         set_food = set(food_times)
#         min_val = min(set_food)
#         if len(food_times) < 1:
#             return -1
#         leng = len(food_times)  # 남은 food_times의
#
#         # mX_공통된 영역씩 *k초씩 진행
#         if k <= leng * min_val:  #
#             index_index = leng % k + 1  # 남은 food_times배열에서의 인덱스
#             answer = left_index[index_index]  # 진짜 음식번호
#             #  ex_1,3
#             break
#
#         # min_val인 곳들 제거/배열과 인덱스배열/_for##
#         j = 0  ##
#         total = 0
#         for i in (food_times):
#             # del foodtimes[index] min for 위치들 제거
#             #
#             if (i == min_val):
#                 food_times.remove(min_val)
#                 del left_index[j]
#             j += 1  ##
#             food_times[j] -= min_val
#             total += food_times
#
#         if total >= k:
#             return -1
#
#         k -= len(food_times) * min_val  ##공통된 s 지남
#
#     return answer


# - 느낀점
# > 대체법 : '새로'. '다른 자료형'에 저장
# : 인덱스도 같이 저장할 수 있고 등
# : 우선순위 큐
# > 핵심 알고리즘은 해설과 거의 동일한데, 제대로 구체화/구현을 못해냄.
# : 아는 함수 및 자료형 부족

# 해설
# - 우선순위 큐(최소 힙)에 음식 시간, 음식 번호를 튜플 형태로 삽입
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # 1) 공통된 영역*leng초씩 횟수 진행[while]
    # ex_10, 11, 9, 4 -> 4씩 빼 ->
    # ex_6, 7, 5
    # sum_value + (현재의 음식 시간[최소. 공통 부분값(ex_6)] - 이전 음식 시간) * 현재 음식 개수 <= k # 공통 부분 회전 내이라면[(10-4)x3=18<k]
    while sum_value + ((q[0][0] - previous) * length) <= k: # ex_4씩 뺀 걸 저장하지 않고, 본인 총 시간 항상 유지 & 바로 이전 최소값 항상 뺴고 다녀
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length # 공통된 부분[ex_6] 한방에 씩 다 뺴
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 2) 공통 아닌 횟수 남음
    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호[1] 기준으로 정렬 <-> 난 index_index에 살아남은 음식, 순서 저장했었음
    return result[(k - sum_value) % length][1]
    # [남은 회전 횟수 % 남은 길이]번째의 [1_음식 번호] <-> 내가 +1이던건, 음식번호 1,2..저장을 [0],부터 저장했기에

