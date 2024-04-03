# - 푼시간 측정 좀 부정확 
# (( 사유_어제 풀다가 마우스 패드 조작 실순지(마우스 패드 종종 버벅댐 약 7년썼으면 놑북은 나름 잘 버티는 중 일 수 있음ㅎ...ㅋㅋㅋㅎ) 페이지 초기화되는 거 눌러서 다시 품. 다시 읽고 정리도 해야하니 감안하여 +=7분했음))

# 1)
# 뽑기 : (빈 곳 뽑기 가능) 값(0빔 1~100) 
# 같은 모양 두 개 쌓음 -> 터짐 : 터진 개수

# 2) 이번에 뽑는 거(get)-> 열_[get-1] 행_not 0
# : 어차피 인형 새로 넣기나 옆으로 이동은 없음.
# :: m1 0빼고 열기준 새로저장 m2 인덱스 차례 계산

# m2 : index_i_row=[0]*w # 각 열의 맨 위 행인덱스

def solution(board, moves):
    answer = 0
    w= len(board[0])
    h= len(board)
    index_i_row=[0]*w 
    
    store=[]
    for get in moves : # 5 번째 열
        # j=0 # 다음 행으로 넘어갈 때 이미 j 대신 index_i_row 값을 1 증가시켜줌. ((두 방법 다 하면 안됨))
        while(1):# 인덱스 #뽑을 놈 위에서부터 찾는다~ ##그냥 바로 아래에서 조건문으로 동일한 거 적음X while(index_i_row[get-1]<=h-1):
            row_i= index_i_row[get-1] # +j하면 안됨
            if row_i >= h : # 바닥까지 봤는데 0만 있었다.
                break
            target = board[row_i][get-1]
            # print('행,열,값', row_i+1,get,target) 
            if target == 0 : # 0이면 다음행 
                index_i_row[get-1]+=1 #이 계산으로 깊이 초과하면 나중에 인덱스 에러 안나게 해야함.             
            else : # 뽑을놈 찾았음
                board[row_i][get-1]=0 #뽑아 썼으니까 최근 조회 위치 비우기
                if len(store)!=0 and store[-1]==target : # 같은놈들 터짐
                    answer+=2
                    store.pop() # 이번 타겟은 안 집어 넣었으니 두번 pop 하면 안 됨
                else :
                    store.append(target)
#                 # - 조건에 따른 연산 관찰후 -> 조건 간단화 배치만 한 게 위 코드.
#                 if len(store)==0: 
#                     store.append(target) 
                    
#                 else : # 저장된 거있음
#                     if store[-1]==target : # 터짐
#                         answer+=2
#                         store.pop() # 이번 타겟은 안 집어 넣었으니 두번 pop 하면 안 됨
#                     else : # 맨 위에 다른 모양 있음
#                         store.append(target)

                break
    return answer
# t_53m / 성능_+4 / 최대t_2.26ms 
# ; '변수이름 짧게 &  _ 지양' (한 눈에 코드 파악에 어려움)

# - 다른 사람 풀이
# > 보드 바닥으로 가며 값 살피기 
# : 내가 for len 안 쓴 이유 : 항상 맨 위부터 안 찾아봐도 되게 index_~에 저장해놓는 방법으로 품
# -> 어차피 효율제한 조건 널널하니까, 그냥 for for이 푸는 속도 훨 빨랐을 듯

# : 나_while & 조건 <-> for & break : j in range(len(board)): 
#  [1] 봉원사스님 , 최승호 , mjjin0103 , milliwonaire 외 237 명

