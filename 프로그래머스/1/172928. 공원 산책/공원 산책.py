# 0) park	routes	result
# ["SOO","OOO","OOO"]	["E 2","S 2","W 1(1~9라 ㄱㅊ)"]	[2,1]

# 1,2)
# 길_'O'_0, 장애물_'X'_1 / 방향 거리
# 명령 수행 조건 : 공원 벗어나는지 : 이동중 장애물 있는지 sum( [:])>0

# 2) drc={N : [-1,0], S:[1,0], W:[0,-1] , E:[0,1] }
# for park : s_posi&0 O_0 X_1
# -> for routes : target=posi+drc[command[0]] *[ command[2],command[2]]
def solution(park, routes):
    answer = []
    drc={"N" : [-1,0], "S":[1,0], "W":[0,-1] , "E":[0,1] } # ; 따옴표
    park2=[ [0]*len(park[0]) for _ in range(len(park) )] # ; range(len()
    for i in range(len(park)) :
        for j in range(len(park[0])):
            if park[i][j]=='S':
                posi=[i,j]
                park2[i][j]=0
            else:
                park2[i][j]=0 if park[i][j]=='O' else 1

    for command in routes : 
        # 명령 수행 조건 : 공원 벗어나는지 / 이동중 장애물 있는지 X_sum( [:])>0
        target=[0,0]
        for a in range(2) :
            target[a]=posi[a]+drc[command[0]][a] *int(command[2]) # ; target'[a]' 같은 거 주의.
        # numpy와 달리 +가 elementwise아님
        
        if target[0]>=0 and target[0]<len(park) and target[1]>=0 and target[1]<len(park[0] ):
            # 장애물 없으면 움직이기 # 북 [-1,0]  #park2[posi[0]:target[0]+1][posi[1]:target[1]+1]
            posi2,target2=posi,target
            if posi[0] > target[0] or posi[1]>target[1] :# min() : 같거나 작은거
                posi2,target2=target,posi

            if command[0] == "S" or command[0] == "N":
                # [posi[1]:target[1]+1])
                if sum([ park2[ i ][posi[1]] for i in range(posi2[0],target2[0]+1) ])==0:
                    posi=target

            else :
                if sum([ park2[posi[0]][ j ] for j in range(posi2[1],target2[1]+1) ] )==0: #X_sum(park2[posi[0]][posi[1]:target[1]+1])==0:
                    posi=target                
    return posi
# - 질문하기 봄 & 1h30m / +2 인듯 / 최대 1.01ms 
# - 오래걸린 이유 
# : 리스트 형식 및 함수 잘 모르고 씀

# - 75점 디버깅
# : 정답이 좌표라 우연히 맞을 가능성은 적으니, 이정도 점수면 논리는 맞고 엣지 케이스를 잘 못다룬듯? 
# -> 논리도 꽤나 틀림. 케이스가 값이 감소하는 쪽은 훨씬 적게 있었나봄

# > 질문하기_오류케이스 획득
# : 그 사이에 장애물 있는지 ":로 확인할 때, 인덱스는 값의 대소 관계에 영향받"는 거 놓침

# > TypeError: 'int' object is not iterable : for

# - slicing 주의 : 열만 못 뽑아 /  2차원 sum은 안됨 
#     park2=[[1,2,3],[4,5,6]]
#     print(park2[:][1]) # 이게 1열이 아니라, 1행이 출력됨.(단일 슬라이싱 연속 ) ((park2[:]=park2)[1]))

# - for_range(k,k) 동일값_범위값 없음_에러나는지 : 에러는 안나고 그냥 넘어가짐. 
# : for a in range(1,1): #  
# - a[k:k]에러 체크 : # []출력 (( 길이가 0인 리스트였어도 동일 # 아예 대상인 인덱스가 없다로 돼서))
# b=[]
# print(b[10:10]) 

# - 다른사람 풀이
# : 거리만큼 움직이면서, X있나 확인 <-> 나_X를 1로 맵팽하고 덧셈이 0초과인지 : 근데 처음 생각과 달리 sum이 한 번에 안돼서 오히려 더 복잡해진듯(어차피 sum 때도 돌아야하고.)
