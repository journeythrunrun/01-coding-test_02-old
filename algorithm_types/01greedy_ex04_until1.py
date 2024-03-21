    # 1을 1로 만드는 최소 횟수
    # iii) N==1
    # i) N-1
    # ii) N/K (나누어 떨어지는 경우)
    # 입력 N_17 >= K_4
    #
    # 4) Other Method_speed : 수학적
    # 3) case : 28/4=7 -> 나누기만 해서는 1이 될 때까지 나눌 수 있는 숫자는 어떤 수의 제곱 꼴

N,K=map(int, input().split())
count=0

while(1) :
    if N==1 : #iii)
        break

    elif N%K==0 : #ii)
        N=N/K
    else :#i)
        N=N-1
    count+=1

print(count)
