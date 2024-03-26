# 1. 문제 :
# 2.3. 아이디어 : 코테용 종이로 씀
# 4. 코딩
inpu=list(  input())

result=0
lista=[]
for i in inpu:
    if ord(i) <= ord('Z') and ord('A')<=ord(i):
        lista.append(i)
    else :
        result += int(i)
lista.sort()
for i in lista : # 해설 = ''.join(result)로 한 방.
    print( i,end='')
print(result,end='')

# 12m
# 느낀점 : # 해설 = ''.join(result)로 한 방.