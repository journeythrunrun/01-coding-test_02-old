    # 행에서 가장 낮은 숫자가 뽑아질 때 > 행 중 가장 높은 숫자를 뽑는 행의 높은 수
    # min비교
    # 입력_N행 M열

N, M = map(int, input().split())
max_0=0
for i in range(N):
    matrix =list(map(int, input().split()))
    matrix.sort()
    if matrix[0]> max_0 :
        max_0=matrix[0]
print (max_0)
