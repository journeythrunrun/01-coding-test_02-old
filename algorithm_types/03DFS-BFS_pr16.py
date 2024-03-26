# https://www.acmicpc.net/problem/14502

# 나
# : (해설보다) 4배 빠름. 메모리 조금 덜 사용
# : 1) 벽 3개 선정_'첫번째'라는 의미->'세번째' 세개         <-> [해설] # 1) 벽 3개 선정 중_DFS
# : 2) [3개선정 완료후] 바이러스 전파될 저장소 따로 저장 (copy.deepcopy)
# : 3) 바이러스 전파_DFS
# : 4) 결과점수

# 64_C_3 < 100,000

# - 목차
# : 나_다시 풀기 (함수_전역변수_list형)
#   & 함수_전역변수_int [재귀때_지역번수처럼[함수탈출시] 반환값받으며 이용해야(#@로 표시)<->?dfs처럼 함수끝날때 변수 값 버리는 것과 반대]
# : > 나_풀이
# : > 해설

# - 빨리 다시 풀어보기  
# > 틀렸던 이유 : 함수에 전역int형&재귀함수에서 생각한 전역대로 작동안함 =>초간단_전역리스트형
import copy
n,m=map(int, input().split())
map0=[]
for _ in range(n):
    map0.append(list(map(int,input().split())))

loca_0 =[]
loca_1=[]
loca_2=[]
for i in range(n):
    for j in range(m):
        target=map0[i][j]
        if target == 0:
            loca_0.append([i,j])# 행, 열 > append[=행넣기] > k행 2열
        elif target==2:
            loca_2.append([i,j])
leng=len(loca_0)
new_wall=[] # 한 행당 한 탐색
for i in range(leng-2): # n-3, n-2
    for j in range(i+1, leng-1):
        for k in range(j+1,leng):
            new_wall.append(loca_0[i]+loca_0[j]+loca_0[k])# [2,3] + [ ] +  [ ]
dr=[1,-1,0,0]
dc=[0,0,1,-1]
left=[0]
def virus(r,c): # 2,3
    for k in range(4):
        newr =r+ dr[k]
        newc =c+ dc[k]

        if (0<=newr) and (newr <n) and (0<=newc) and (newc<m):
            if new_map[newr][newc]== 0:
                new_map[newr][newc]=2
                left[0]-=1 ## 리스트_전역리스트 함수 내에서 막 사용 가능_"주소 참조"라, 함수 탈출할 때도 (깊은 곳에서 할 떄 이미 본질적인 값 바뀌어놔있음)
                            # <-> 상수_함수에 전달해야, return도 해야하고(함수전부 탈출한 후에도 가장 깊은 함수에서의 값 가지고 싶으니까.)/생각한 값 바로 안 나오고 복잡한듯. 아마 사라져서인가, 파이썬 강노 참고하든
                virus(newr,newc)# 새로운 2니까

#2)
result=0
for i in new_wall : #[2,3] + [] +  [] # 10개 이하
    new_map=copy.deepcopy(map0)
    # loca_2는 바이러슨데 왜 추가 시킨겨..벽인디 문제 순간 잘못 기억한듯
    # => 변수이름 = 의미로. 값 말고.
    # loca_2.append([i[0],i[1]])&pop했었..벽이어야
    # loca_2.append([i[2],i[3]])
    # loca_2.append([i[4],i[5]])

    new_map[i[0]][i[1]]=1 # 3개 선택했으면 값 바꿔야지
    new_map[i[2]][i[3]]=1
    new_map[i[4]][i[5]]=1

    left[0] = leng-3 # 꼭 3개 세워야하니까.

    for j in loca_2: # [2,3]
        virus(j[0], j[1]) # 리스트 주소로 넘겨버렸던듯
    #3) 안전영역 저장
    result=max(result,left[0])

print(result)
# - 함수_전역변수_int형
import copy
# n,m=map(int, input().split())
# map0=[]
# for _ in range(n):
#     map0.append(list(map(int,input().split())))
#
# loca_0 =[]
# loca_1=[]
# loca_2=[]
# for i in range(n):
#     for j in range(m):
#         target=map0[i][j]
#         if target == 0:
#             loca_0.append([i,j])# 행, 열 > append[=행넣기] > k행 2열
#         elif target==2:
#             loca_2.append([i,j])
# leng=len(loca_0)
# new_wall=[] # 한 행당 한 탐색
# for i in range(leng-2): # n-3, n-2
#     for j in range(i+1, leng-1):
#         for k in range(j+1,leng):
#             new_wall.append(loca_0[i]+loca_0[j]+loca_0[k])# [2,3] + [ ] +  [ ]
# dr=[-1,0,1,0]
# dc=[0,1,0,-1]
#
# def virus(r,c,left): #@@
#     for k in range(4):
#         newr =r+ dr[k]
#         newc =c+ dc[k]
#         #print(newr,newc)
#         if (0<=newr) and (newr <n) and (0<=newc) and (newc<m):
#             if new_map[newr][newc]== 0:
#                 new_map[newr][newc]=2
#                 left-=1 #@@
#                 left=virus(newr,newc,left) #@@
#     return left #@@
# #2)
# result=0
# for i in new_wall : #[2,3] + [] +  [] # 10개 이하
#     new_map=copy.deepcopy(map0)
#
#
#     new_map[i[0]][i[1]]=1 # 3개 선택했으면 값 바꿔야지
#     new_map[i[2]][i[3]]=1
#     new_map[i[4]][i[5]]=1
#
#     left = leng-3 # 꼭 3개 세워야하니까.
#     #print(new_wall)
#     for j in loca_2: # [2,3]
#         left=virus(j[0], j[1],left) #@@
#     #3) 안전영역 저장
#     result=max(result,left)
#
# print(result)



# - 내 첫 정답풀이
# n,m=map(int, input().split())
# rowc=[]
# 
# for _ in range(n):
#     rowc.append( list( map(int,input().split())) )
# 
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
# 
# result=0
# def virus(x,y):
#     for i in range(4): # 1))_1 새 위치 가지
#         nx=x+dx[i] # 1))_2 새 위치
#         ny=y+dy[i]
#         if nx>=0 and nx<n and ny>=0 and ny<m: ##1))_3 새위치 멀쩡한지
#             if temp[nx][ny]==0: #2)) 타겟 값조사 # 0이어야지 2가 다음으로 확산. 다른 2 만났을 땐 그 virus따로 넣어줄 거
#                 temp[nx][ny]=2 #3)) update
#                 virus(nx,ny) # #4)) 그 요소가 이어서_dfs
# 
# 
# # 안전 영역 계산
# def get_score():
#     score=0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j]==0:
#                 score+=1
#     return score
# 
# empt=[]
# wall=[]
# biru=[]
# for i in range(n):
#     for j in range(m):
#         if rowc[i][j] == 0:
#             empt.append([i,j])
# 
#         elif rowc[i][j]==1:
#             wall.append([i, j])
# 
#         elif rowc[i][j]==2:
#             biru.append([i, j]) # leng행 2열
# 
# 
# leng_e=len(empt)
# target=[]
# # 1) 벽 3개 선정_앞->뒤 세개 #
# for i in range(leng_e): # 가장 앞 index가 [i]일 때
#     for j in range(i+1,leng_e):
#         for k in range(j+1,leng_e): # j+1 <- i+2
#             temp2=empt[i]+empt[j]+empt[k]
#             target.append( temp2 ) # [2,1,3,4,5,6]
# 
# 
# # from collections import deque
# # # bfs
# # queue=deque()
# # visited=[[0]*m for _ in range(n)]
# 
# #
# import copy
# temp=[]
# for i in target:
#     temp = copy.deepcopy(rowc)
#     temp[i[0]][i[1]]=1
#     temp[i[2]][i[3]] = 1
#     temp[i[4]][i[5]] = 1
#     print(biru)
#     for b in biru:# [2,3] [4,5]  / virus 함수에서 맵의 값이, 큰 for 문 돌 때마다 바뀜 -> 맵 temp로 따로 저장
#         virus(b[0],b[1]) # 바이러스 먹은것도 rowc로 하면 잃어버림 -> 함수에서 temp로 사용. 근데 주소로 해버리려나.
# 
#     # tap 하면 안되지..
#     result = max(result, get_score())
# 
#         #r,c=b[0],b[1]
#         #queue.append([r,c])
# 
# print(result)
# #math.comb(len(rowc),2)


# - 해설
# 1) 벽 3개 선택_dfs로 함. 근데 저렇게는 조합 경우의 수 넘지 않나. nxm_C_3 ->
# n,m=map(int, input().split())
# data=[]
# temp=[[0]*m for _ in range(n)]
#
# for _ in range(n):
#     data.append(list(map(int, input().split())))
#
# dx=[-1,0,1,0]
# dy=[0,1,0,-1]
#
# result=0
#
# #dfs_바이러스 퍼지기
# def virus(x,y):
#     for i in range(4):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if nx>=0 and nx<n and ny>=0 and ny<m:
#             if temp[nx][ny]==0: # 0이어야지 2가 다음으로 확산. 다른 2 만났을 땐 그 virus따로 넣어줄 거
#                 temp[nx][ny]=2
#                 virus(nx,ny) # dfs
# # 안전 영역 계산
# def get_score():
#     score=0
#     for i in range(n):
#         for j in range(m):
#             if temp[i][j]==0:
#                 score+=1
#     return score
# # 'dfs' 로 울타리 설치하면서, 매 번 안전 영역 계산[n*m]
# def dfs(count):
#     global result
#     #
#     if count==3:
#         # 2) [3개선정 완료 후] 바이러스 전파될 저장소 따로 저장
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j]=data[i][j] # temp : 바이러스 전파로 업데이트될 값 저장할 장소
#
#         # 3) 바이러스 전파
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j]==2:
#                     virus(i,j)
#         # 4) 결과점수
#         result=max(result,get_score())
#         return
#     # 1) 벽 3개 선정 중_DFS
#     for i in range(n):
#         for j in range(m): #0이 있는 거에서 돌지 말고, 그냥 nxm 맵에서 돌아
#             if data[i][j]==0: # 첫 번째 벽 세울 위치 = [i,j] => (가장 바깥 for문 거치며) ㅠ로 뽑는듯 C말고.
#                 data[i][j]=1
#                 count+=1

#                 dfs(count) ## count만 전달 / count를 return은 안 하네 : forward로 3되고 나서는 안쓰임.
#                            #back은[함수 탈출하며] 값 상관없음.
#                 data[i][j]=0 ## 한 벽 선택하고 관련 계산 끝나서 함술 탈출했으면, 해당 벽 다시 원래 값화.
#                 count-=1
#
#
# dfs(0)
# print(result)
