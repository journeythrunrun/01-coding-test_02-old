# 1. 문제 : 출발할 수 있는 최대 그룹수
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
N=int(input())
a=list(map(int,input().split()))

a.sort(reverse=True)
stacked_index=0 # 출발할 그룹의 공포도를 결정할_인덱스
count=0
previous=a[0] # 공포도
while (previous <= N-(stacked_index)): #(stacked_index+previous<= N): #$ 1) N-1까지니까  # 다음 그룹 인덱스가 N초과하면 남은 애들 출발 못해서 break [1]
    # 1) a[0]_3 a[1] a[2] / 2) a[3] : '2'까지 있으면 count. 다음에 사용할 index는 '3'
    count+=1    #1) 출발

    if (stacked_index+previous > N-1 ):# 2) next index가 리스트 초과 경우
        break
    previous,stacked_index=a[stacked_index+previous],stacked_index+previous # 다음 # 원래 남았던 인덱스 + 공포도
                            # 동시에 바뀌어서 따로 하면 서로 영향줘서 값 이상해짐  # 인덱스 선택_stacked_index+previous
print(count)

# [1] 다른 시각 설명
# if previous > N-(stacked_index): # 공포도_다음인덱스 필요한 명수 > 남은 명수(본인포함)_a[]뒤
#    break