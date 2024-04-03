# 0)
# s	skip	index	result
# "aukks"	"wbqd"	5	"happy"
# 1) s의 알파벳을 index숫자 만큼의 다음 알파벳으로 전환할거임 (z->a)
# 이때 skip에 나온 알파벳은 제외하고 셈


# 12) ord(a)+index & skip알파벳 건너 뛰기 & z넘으면 a로

# Again 2)
# for in s _ while(index끝날때까지) _ not in skip(딕셔너리/셋화)이면 index-=1 / 다음문자=chr ord a if ==z 
def solution(s, skip, index):
    # ord<-> m2)for abcd돌아가기
    answer = ''
    # m1) skip에 따라 0,1저장하고 -> index+from_skip[:] 더해서 알파벳 하려했엇음.       # save=[1]*26
    
    # X_딕셔너리법은 [:]대체 귀찮
    # for a in skip :
    #     # skip개수 만큼 더 더해. z넘어가면 수식 만들기 귀찮다<-> while로 걍 알파벳 돌자.
    #     save[ord(a)-ord('a')+index+]
    # m2)
    dict1={}
    dict1=dict1.fromkeys(list(skip),1) ##
    print(dict1)
    for cha in s :
        count=0
        i=1
        while(1): #  뭔가 더 복잡해졌
            # 1씩 증가하며 알파벳 도는 i / z 다음은 a화
            # ord(cha)+i=ord('a') case
            i= ord('a')-ord(cha) if ord(cha)+i> ord('z')  else i #조건문 대신 계산식 귀찮아 temp = (ord('z')-ord(a)+i) %26
            obj= chr( ord(cha)+i) 
            if obj in dict1 :
                pass
            else : # count
                count+=1
            if count==index:
                answer+=obj
                break
            i+=1
    return answer
# : 뭐지 아까 왜 정확성 10%나왔지. 뭐 잘못건드렸었나 
# : 49m / 성능 +8 & 최대0.37ms

# - 다른 사람 풀이
# > string.ascii_lowercase 로 a~z한방에 가져옴.
# > set화 : a~z, skip
# -> set-set을 통해, 돌아가는 알파벳 대상을 줄임
# -> sorted(set1) 리스트화
# -> 알파벳 대상이 줄여진 리스트의 인덱스를 value값으로 딕셔너리에 저장.
# -> index 칸만큼 넘어가는 연산에서 사용 [ %len ]
# > sorted(set1) : 입력_set가능 / 출력_list

# from string import ascii_lowercase
# def solution(s, skip, index):
#     result = ''

#     a_to_z = set(ascii_lowercase)
#     a_to_z -= set(skip)
#     a_to_z = sorted(a_to_z)
#     l = len(a_to_z)

#     dic_alpha = {alpha:idx for idx, alpha in enumerate(a_to_z)}

#     for i in s:
#         result += a_to_z[(dic_alpha[i] + index) % l]

#     return result
# [1] HardM00N , fall031-muk , 맹구 , 김재윤 외 12 명