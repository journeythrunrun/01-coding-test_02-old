# # 19 나_해설 후_https://www.acmicpc.net/problem/14888
#
n =int(input())
numbers = list(map(int, input().split()))
plus, minu, mult, divi =map(int, input().split())
# n-1개 써야 하니
result=numbers[0]
max0=-1e10 #
min0=+1e10

# 한 함수 벗어날 때의 result값은, result가 global이 아닌 int형이라서 이전의 값으로 자동.
def go(count, result):
    global plus, minu, mult, divi,max0,min0 # 전역_int형을 함수 안에서 사용하기 위해 : global
    if count==n-1:
        max0=max(max0, result)
        min0=min(min0,result)
        return
    if plus >0 :
        plus-=1
        # [count+1] 인거 : count에 비례하는 건 아니까, 특정값 하나로 찾는 게 빠름
        go(count+1, result+numbers[count+1]) # count+1번째계산수행완료한 것 result로 전달
        plus+=1
    if minu >0 :
        minu-=1
        go(count+1, result-numbers[count+1])
        minu+=1
    if mult >0 :
        mult-=1
        go(count+1, result*numbers[count+1])
        mult+=1
    if divi >0 :
        divi-=1
        go(count+1, int(result/numbers[count+1]) )
        divi+=1
go(0,result)

print(max0)
print(min0)


# # - 다른 방법 _ 중복 순열
# from itertools import product
# # 중복 허용 3개 뽑기
# print(list(product(['+','-','*','/'],repeat=3)))

#$ 경우의 수_n개 픽 채워야하니_가장 깊게까지 가는 dfs
#$ 병렬 스택[dfs] 아름답게 쌓았네 [if 병렬_if 탈출하며 다른 경우로 가게]
#$ 파라미터?(사용한 연산자 수, 현재 연산결과) 전달
#$ 함수 탈출=트리그림 한층 위 =>트리 가지(경우)선택 =조건문_2)
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n: #$ 1) 가장 깊은지 체크
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        #$ 2) 어떤 스택[경우] 갈지 선택
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            # 3) dfs로 끝까지 갔다가 함수 탈출했을 때[가지 올라왔으면] : 층 업데이트는 i+1로 해줬던거, 함수 탈출하면서 자동 i

            add += 1 # 이젠 다른 경우의 수 할거니까 add개수 원래대로 돌려놓고 아래 if문_다른 연산자

        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]) )# 음수케이스때문에 //안됨
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)

# # 1. 문제 :
# # 2.3. 아이디어 : 코테용 종이로 씀
# # 4. 코딩
#
#
# import copy
# n= int(input())
# numbers= list(map(int,input().split()) )
# oper_num=list(map(int,input().split()) )
# numb=0
# result=[]
# visited=[False]*(n-1)
# total=[]
# mid=[]
#
# def indexx(numb,k):
#     for i in range( len(numbers) ):
#         if visited[i] == False:
#             mid+=[i] # [ , ...,2,3
#             visited[i]=True
#             numb += 1
#             if numb==oper_num[k]:
#                 result.append(mid[-numb:])
#                 return result
#
# temp_visi=copy.deepcopy(visited)
# plus=indexx(0, 0) # [2,4]
# minus=indexx(0, 1) #[1,3]
# mul=indexx(0, 2,visited)
# divi=indexx(0, 3)
# temp=0
# for i in range(n-1):
