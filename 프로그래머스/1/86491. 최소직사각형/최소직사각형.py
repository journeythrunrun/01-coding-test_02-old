# 최소직사각형_https://school.programmers.co.kr/learn/courses/30/lessons/86491
# => max를 가진 가로 혹은 세로의 나머지 까지 저장 
# : m1) max값 두가지씩? 100 9, 90 1 /1 100 2 99 
# : m2) sort?
# ( sizes= 안빔, 자연수 )

#_	통과 (6.11ms, 11.3MB)
def solution(sizes):
    # 정렬효율? # 정렬이 접근n보다 더 시간 걸림.


    # k개 까지의 최소 명함하며 완전 탐색이 가능할까? 
    # <-> 반례: 60 50, 70 100  : 70 100이 낳을지 100 70이 나을지 나중에 나오는 거 알아야 최적화<->나왔을 때 갱신하면 되지. 

    big, small=1,1 # max()로 순서부여(정렬)_뒤집가능 무시
    #    side=[[1,1],[1,1]]
    for a,b in sizes :
        # maxv,minv=max(a,b),min(a,b)# 가로세로 무시
        # # 둘다 클때 # 엄밀 최적해 방법 헷갈릴때 = (for안) 조건_경우의 수 쪼개서 생각
        # if maxv >= big and minv >=small :
        #     big, small =maxv,minv
        # # 한쪽이라도 클 떄 # 60 30<- 70 30
        big, small = max( max(a,b) , big), max( min(a,b), small) # 압축본
#         elif maxv >= big :
#         elif minv >=small :
    return big*small
# -해설[압축]