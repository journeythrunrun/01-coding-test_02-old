# 1. 문제 : 럭키 스트레이트
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
n=list(input() )

a=[0,0]
for i in range(len(n)):
    if i  >= len(n)/2 : #ex_0,1,2,3 / 4
        a[1]+= ord(n[i])-ord('1')

    else :
        a[0]+= ord(n[i])-ord('1')
if a[0]==a[1]:
    print("LUCKY")
else :
    print("READY")

# - 10m
# - 느낀점
# : 코테 연습 하니까 코테에 쓰이는 문법이 조금씩 익숙해진다.
