# bandage	health	attacks	result
# [5_기술 시전 시간, 1_초당 회복량, 5_추가회복량]	30_최대체력	[[2, 10], [9_공격시간, 15_피해량], [10, 5], [11, 5]](시간_오름차순/중복없음)	-> 5_마지막 공격후남은 체력 / 0이하 : -1 


# 1)
#: t초 동안 붕대 감으면서, 1초마다 x만큼의 체력 회복 / t초 연속 붕대감기 성공 시 +=y
#: 최대 체력

# : 공격(-=) 받 : 쓰는 중인 기술 있으면 취소, 체력 회복 할 수 없는 순간.(연속 붕대감기 0) 
# : 기술 끝나면 붕대감기,

# ; 0 이하 : 캐릭터 죽음.
# 2) 값 적으니까, for i in (1, attacks[-1][0]+1)<-> 수학적연산

def solution(bandage, health, attacks):
    answer=health #~ 시작이
    idx,inter,extra=0,0,0 # inter : 누적
    for i in range(1, attacks[-1][0]+1) :# <-> 수학적연산
        if i==attacks[idx][0] : # 공격 받는 시각
            answer-=attacks[idx][1]
            idx+=1 # 다음 공격
            inter=0 # 초기화
        # elif <health : # min으로 대체_최대 체력보다 적으면 체력충전 
        else : # not 공격 & 충전
            inter+=1 #먼저있어야  # for에서 25 30 , ㄴ
            if inter==bandage[0]  : #누적충전&일반충전
                print(inter, bandage[0])
                answer= min(answer+bandage[1]+(bandage[2] ), health)# 최대 체력이나 충전체력   
                inter=0
            else : # 일반충전
                answer= min(answer+bandage[1], health)
                
        print(i,answer,'inter',inter)
        if answer <= 0 : # ;이미 죽어야
            answer=-1
            break

    return answer # 마지막에 죽는거 확인_하면 안됨.
# : 41m / 성능 +3 / 1.73ms
# - 쉬웠는데 오래 걸린 이유 : 문제 정리에 시간 썼나? / 논리 조건 설계가 빠르진 못했다?

# * ; 제출 전 : 입출력 예와 중간출력 다 일치하는지 확인

# - 디버깅
# : 체력 0이하면 이미 죽어야함 -> 문제 풀 때 연산/조건체크 수행하는 단계(위치) 함부로 뒤쪽에 압축하면 안됨

# - 다른 사람 풀이
# : m2_수학적연산_ ((for in attacks : 나도 수학적연산화 만들수 있을 것 같으니 굳이 다른 알고리즘(알아야 풀 수 있는 문제) 연습하기 전에 해보진 않겠음 ))
# def solution(bandage, health, attacks):
#     hp = health
#     start = 1
#     for i, j in attacks:
#         hp += ((i - start) // bandage[0]) * bandage[2] + (i - start) * bandage[1]
#         start = i + 1
#         if hp >= health:
#             hp = health
#         hp -= j
#         if hp <= 0:
#             return -1
#     return hp

