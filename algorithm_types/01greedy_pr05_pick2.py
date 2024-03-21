# 1. 문제 : 볼링공 고르기
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
## 문제 잘못 이해 :
# data_set = set(data)
# leng=len(data_set)
# print( leng*(leng-1)/2 )
##

N, M= map(int,input().split() )
data = list(  map(int,input().split() )  )

count=0
for i in data: # method for my time
    for j in data:
        if i!=j :
            count+=1
print(int ( count/2) )
#17m