# 1~45 중 6개
# 1_6개 맞춤 2_5 3_4 4_3 5_2 6(낙첨)_1이하_0,1
# -> 순위 출력


# 2)
# in 충족 개수-> 최고_+=0의개수 / 최저_.
# sort 굳이 ##

# 괜히 m2 효율화한다고 [6초기화 & -= 연산법 써서] 코드 작성 속도 더 번거로워짐.

# m1
# def solution(lottos, win_nums):    
#     answer = [0,0]
#     # sort _nlogn 이용한 방법 -> 구현 속도 귀찮음.
#     already=False
    
#     # 괜히 효율화한다고 6초기화 & -= 연산법 써서 코드 작성 속도 더 번거로워짐.
#     # 논리 엄밀 체크으
#     for a in lottos :
#         # 한 번은 패쓰
#         if a==0:
#             # print(a) # 위치제한 없을 것 같은데말얌
#             # if already == False : # 1개는 맞추어도 순위 그대로임.
#             #     already =True
#             #     continue
#             answer[0]+=1
            
#         elif a in win_nums :
#             # print(a)
#             # if already == False : # 위 조건이랑 똑같은 패러다임이 들어가면 안되지. 연산하는 게 다르잖아.
#             #     already =True
#             #     continue
#             answer[0]+=1
#             answer[1]+=1
            
#     return [ 6 if a<=1 else 7-a for a in answer]
# 0.01ms

# m2) > 논리 엄밀 체크용 진행
def solution(lottos, win_nums):    
    answer = [7,7]
    # already=False
    
    # > 논리 엄밀 체크으
    # : 두 조건에 의한 게 차이가 나는 경우 : "로또 맞추는 거에는 순서가 없는데, 코드적으로는 0이 먼저나오는것/숫자로 맞추는 것 의 순서에 따라 다른 결과가 나오게 됨. "
    for a in lottos :
        # 한 번은 패쓰
        if a==0:
            # if already == False : # 1개는 맞추어도 순위 그대로임.
            #     already =True
            #     continue
            answer[0]-=1
            
        elif a in win_nums :
            # if already == False : # 위 조건이랑 똑같은 패러다임이 들어가면 안되지. 연산하는 게 다르잖아.
            #     already =True
            #     continue
            answer[0]-=1
            answer[1]-=1
    return [ 6 if a==7 else a for a in answer]

# - 다른 사람 코드. 
# 2) 사전 정의 rank  -->  개수->인덱스사용-> 2) 순위=rank[cnt_0+ans], rank[ans]
# : 0개수 = .count
# def solution(lottos, win_nums):
#     rank=[6,6,5,4,3,2,1] # 2) 랭크에 각 개수에 따른 순위 1대1 맵핑

#     cnt_0 = lottos.count(0)
#     ans = 0
#     for x in win_nums:
#         if x in lottos:
#             ans += 1
#     return rank[cnt_0 + ans],rank[ans] # 2)
# (..... , 박관우 , - , - 외 267 명)
