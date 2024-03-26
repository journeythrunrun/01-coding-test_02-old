# 1. 문제 : 상하좌우
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
present=[1,1]
new=[1,1]
N=int(input() )
path=list(map(str, input().split()) ) ### str

present=[1,1]
new=[1,1]
for i in path:
    new[0],new[1]=present[0],present[1] ## new는 현재 실제 위치로부터 진행해야 하니까.

    if i =='L':
        new[1]-=1
    elif i =='R':
        new[1]+=1
    elif i =='U':
        new[0]-=1
    elif i =='D':
        new[0]+=1
    else :
        print("error1")

    if new[0] > N or new[0] < 1 or new[1] > N or new[1] < 1:
        continue # present 갱신 생략 [이전 것 그대로]
    present[0],present[1]=new[0],new[1] # 새로운 걸로 갱신

print(present)

# 28m
# - 느낀점
# : 리스트 이름으로 = 하면 존재가 복사되버림
