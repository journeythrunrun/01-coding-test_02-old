# - 다음날 복습
# : 코드 실행시간 효율 가장 좋아진듯
import copy
n,m= map(int, input().split())

map0=[]
blank=[]
wall=[]
viru=[]
for i in range(n):
    map0.append(list(map(int, input().split())))
    for j in range(m):
        if map0[i][j] == 0:
            blank.append([i,j]) #[1,2] , ..
        elif map0[i][j]==2:
            viru.append([i,j]) #
dr=[0,0,1,-1]
dc=[1,-1,0,0]
def virus(r,c): #[1,2] 실제 바이러스

    for i in range(4):
        nr=r+dr[i]
        nc=c+dc[i] # 위 등.
        if nr >=0 and nr<n and nc>=0 and nc<m:
            if map2[nr][nc]==0:
                map2[nr][nc]=2
                safe[0]-=1
                virus(nr,nc)

leng=len(blank)

target=[]
for i in range(leng):
    for j in range(i+1,leng):
        for k in range(j+1, leng):
            target.append([i,j,k]) # 벽의 주소에서 [1,2,3] 번째 들 사용할게
# 바이러스 퍼짐
result=0

for i in target: # i=[1,2,3] # 0값의 인덱스 주소 저장해놓은 것들에서, 몇번째 것들 세개를 뽑을 건지
    map2=copy.deepcopy(map0)
    safe = leng - 3

    # 벽 3개 짓기
    map2[blank[i[0]][0]][blank[i[0]][1]]=1 # i'[0]' : i를 새 이름으로 받든.
    map2[blank[i[1]][0]][blank[i[1]][1]] = 1
    map2[blank[i[2]][0]][blank[i[2]][1]] = 1
    # 바이러스 퍼짐
    for j in viru :
        virus(j[0],j[1]) #dfs가 더 쉬움
    result=max(safe[0],result) # 자기 자신 바로 써도 되나 -> 안됨. 우변이 먼저야.
    # 안전 영역 수
print(result)
