# ex 2.1.2) 큰 수의 법칙
### 생각,필기 등 부가적인 내용
### 생각
### : 쉬운 문제라 차근차근 생각법보다 직관적 생각 진입해봄
### 문제 대충 K_번 연속 덧셈 가능<=M_번 더해
### 일단 K번 + M-K번()
### result= aa[0]*k+aa[1]

n,m,k=map(int,input().split())
aa=list(map(int,input().split()))
aa.sort(reverse=True)

next_number=False
result=0
left=m # <- m으로 그대로 써도 되는데 for 코드 의미
while(1): #x for left in range(m,0,-1):# 남은 횟수화
    if left==0:
        break
    if next_number==False:     # i) aa[0]더할 때
        if left >= k :# i_i) 남은 번수가 K번이상
            result+=aa[0]*k
            next_number=True
            left-=k #$ 주의

        else :# i_ii)남은 번수가 K번이하_[0]더할 차례에서
            result+=aa[0]*left
            left-=1
            break

    else :     # ii) aa[1] 더할 때 [ next==True ]
        result+=aa[1] # [@1]
        next_number=False
        left-=1

print(result)

# [@1]
#  aa[0]이랑 aa[1]같아서 aa[1]더해도 자동으로.
# if aa[0]==aa[1]:
#     result+=aa[0]
