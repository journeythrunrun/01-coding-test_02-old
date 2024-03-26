# 1. 문제 : 만들 수 없는 금액
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩

##
# N=int(input() )
# inpu = list ( map(int, input().split() )  )
# inpu_max=sorted(inpu,reverse=True)
# inpu_min=sorted(inpu)
#
# save=[]
# index=0
# for result in range(1000000):
#     if result in inpu : # 만들어야 하는 값
#         save.insert(result ) ## 제거는
#         continue
#     elif  # 만들어야 하는 값 -1은 이미 있을거고, 1있는지 (이미 쓰였을 수도 있어서) ##-> pop ## 맨 앞이랑 맨뒤 더해?
#
#     elif
# print(result)
##

# - 해설 -> 주석 수정
n = int(input())
data = list(map(int, input().split()))
data.sort()

target=1 # 검사대상
for x in data :
    if target < x :# 핵심2 > 만들 수 없는 금액을 찾았을 때 반복 종료
        break
    target+=x # 다음 검사대상
print(target)