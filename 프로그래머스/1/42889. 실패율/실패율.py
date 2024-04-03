# 느리게 푼 원인_sort key 사용법 : 기억 안나서 전부 구현하려다가 시간 꼬임
# 1) 실패율 높은 stage부터 내림차순으로 & 같으면 작은 번호 #~
# 2) 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수[해당stage_count] / 스테이지에 도달한 플레이어 수[s 이상_count  OR  0->전체 0]
#  key ?

# stages : 현재 스테이지

def solution(N, stages):
    # 각 값 count
    coun=[0]*(N+2)
    for a in stages :
        coun[a]+=1
        
    # 스테이지 별 실패율
    # X_m) idx?
    answer=[]
    for j in range(1,N+1): # 1~N
        bb=sum(coun[j:]) # 3) good [시간복잡도 내이면 too much효율 X][ 2)에서 전체 패러다임하니까 구현 시 복잡해져서 놓치는 실수 적네] ( 맨 초반 시도 쯤은, 이걸 굳이 첫 for문에서 전부 연산하며 하려다가 복잡해져서 구현 실수 발생.  )
        if bb==0:
            answer.append([0,j]) # [실패율,스테이지]
            continue
        answer.append([coun[j]/bb,j])
    # 
    # X_m etc)첨에 sort 실행 반대순으로 했었음. 그럼 안됨 최종 sort를 원하는 게 두번째여야.(역순)
    # answer.sort(key=lambda x:x[1]) 
    
    # :: 엥 저번엔 위에 sort도 해야 성공였던 거 같은데 이것저것 시도하다 섞였었나봄
    answer.sort(reverse=True, key=lambda x:x[0]) # [1]도 이 방향으로 정렬되지 않기 위함. [1]의 차순은 미리 입력을 넣어놓은 순.((sort방식에 영향 받을 수도 있나 암튼 그건 테스트셋 결과로 보삼ORsort[1]))
    
#     for j in range(len(answer)):
        
#         if old ==answer[j]:
            
#             if
#         old = j # 음냐냐 집중~
        
    # answer.sort(key=lambda x:x[1]) # key 뭐이런게 있었던 것 같긴함
    
    # print(answer)
    return [ a[1] for a in answer ]

# - 나_최대 13.89ms
# - 다른 방법
# : 나_sum <-> count OR 스테이지 값 저장위해 for돌때 다른 변수에 누적저장((지금 이 부분을 그렇게 자세히 봐야하는가))


# - 오랜만에 코테공부 시작하고 sort key 사용 방법까진 정확히 기억 안나서 구현하려다가 시간 잡아먹은 부분. 생각해내는 연습은, key로 못하는 부분에서 연습하자.
#     # sort가 두번째 요소 어떻게 하지
#     if N==1:
#         return [1]
#     old=answer[0]
#     result=[old[1]] #[old]
#     c=1
#     same=[]
#     for k in answer[1:] : #  4 3 2 1값 같을시 높은 스테이지부터있어버림
        
#         if old[0] !=int(k[0]):
#             same.append(k[1]) # same씩 sort
#             # result.append(old[1]) # 이전스테이지값을 맨 뒤에
#             # result[c-1]=int(k[1]) # 새 값을 앞에
#         else :# ㄷ
#             if old[0] !=int(k[0]):
                
#             if len(same)>=1:
#                 same.sort()
#                 result+=same
#                 same=[]
#             result.append(int(k[1])) #result[c]
#         old=k#result[c]
#         c+=1
#     if len(same)>=1:
#         same.sort()
#         result+=same
#         same=[]                
        
#         # print(int(k[1]))
#     # print(answer)
    
#     return result

# - 세네달전 쯤 하던 거
# # 그 중 클리어못한 / 도달수 =1_ count0-count1_[클리어한 수]/count0 
# # * 도달 없 = 0
# # -> 실패율 높은 스테이지 번호부터 , 내림차순(중복시_작은번호 먼저)

# # N = 자연수, stages= 안빔, 자연수 (N+1은 완료후 멈춤)
# # 40m
# def solution(N, stages):
#     # 돌면서 앞 스테이지 놈들것 까지 더하기?_누적 계산
#     # 값 높은 것부터, 작은 것부터. = -로저장_작은것부터, 작은것부터 
#     # for2 [ a[1] for a in result ] 
#     # *는 같은 행 내에서 concate 확장임.
#     #count=[[0]*(N+2)] #  0,1~N+1  ####~ []뺴면 []sjg넣으면
#     #count=[[0] for _ in range(N+2)] #  0,1~N+1  ####~ []뺴면 []sjg넣으면
#     count=[0]*(N+2)

#     # 걍 효율보다 구현 우선 짜자
#     for i,b in enumerate(stages): # [2,1, ..]  # 1~N+1
#         for j in range(1, b):# 1~b-1 # 1~N
    
#             count[j]+=1 # 1~N
        
#     result=[[0,1]] # 첫요소 1은 실패율 없음
#     for k in range(2,N+1): # 1~N
#         if count[k-1]==0:
#             result.append([0,k])
#         result.append([-(count[k-1]-count[k])/count[k-1] ,k] ) # ~N+1
#     # 너무 돌아서 푼 방법이다.
        
#     result.sort()
#     return [ a[1] for a in result ] 
    

    