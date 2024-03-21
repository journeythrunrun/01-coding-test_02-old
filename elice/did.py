### 1. 6/20 속도
n, m = map(int,input().split())
# 저장소
# a=[[0,0] for ]
###save=[]
a=[]
for i in range(n):
    #a[i]
    a.append( list(map(int, input().split() ) ) )
    ###save.append([0,0])
save=[]
for i in range(2*(10**5)+1):
    save.append(0) ### [0]
##a.sort()
##target=a[M-1][0]#~아 끝나는 시각 반영안했다
for i in range(n):
    first=a[i][0]
    end=a[i][1]# 1 6
    for j in range((end-first+1)): # 몇번
        save[j+first]+=1# +1제거
        #print(save[j+first+1]) ##+=1 # 리스트는 붙여져버림?1인데

one=-1
# 0, 1, 4
exist=False
for i in range(2*(10**5)):
    if save[i+1]>=m:
        print(i+1)
        exist=True
        break
if exist==False:
    print (one)


## 2. 너무 쉬운 문제
# the_world_is_flat = True
# if the_world_is_flat:
#     print("Be careful not to fall off!")
n, k= map(int, input().split()) # 1부터 k 개의 구역

inpu=list( map(int, input().split()) )

result=0
for i in range(k):
    result+=inpu[i]

# 그냥 무식하게 하는 게 젤 간단할듯
old=inpu[0]
new=result
for i in range(n-k):
    new=new-old+inpu[i+k]
    if new>result:
        result=new

    # if inpu[i+k]> old:
    #     result=result-old+inpu[i+k]
    old=inpu[i+1]

print(result)



### 3.
n,k = map(int, input().split())

# 1시간 47분남음






