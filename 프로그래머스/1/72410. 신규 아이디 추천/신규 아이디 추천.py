# 1)
# 길이(3~15), 소문자,숫자, -, _, .(처음끝x, 연속x)
# 2) 
# i) 대문자->소문자 ord
# ii) 다른 글자 제거

# 마침표 연속 시 1개 남기고 지우기 /처음끝 체크하며  지우기

# -> if len(new)==0 : new="a" / elif len(new) >=16 : new=new[:16] 
# --> if new[15]=='.': new=new[:15] 마지막 .인지 while()
# if len(new)<=2 : 길이 3까지 new+=new[-1]
def solution(new_id):
    answer = ''
    dict1=dict()
    
    temp=list(range(ord('a'),ord('z')+1) ) + list(range(ord('1'),ord('9')+1) )+[ord('0')]+ [ord('-'),ord('_')]# .은 따로해줄거임 # 사용형식주의_조건에서 전부 ord로 하고 있음. 저장도 ord.
    sett=dict1.fromkeys( temp  )

    dotal=False
    for cha in new_id :
        ordA=ord(cha)
        if ordA>=ord('A') and ordA<=ord('Z'): # 대문자
            answer+=chr( ordA-( ord('A')-ord('a')  )  ) # 소문자화 # x-X=y-Y
        # elif ordA not in sett : # 아예 다른 문자_자동으로 answer에 안붙임
        #     pass
        # 설명은 원래 꺼를 지우고 바꾸는 흐름이고, 나는 answer에 새로 만들어주는 흐름이라 다름. 그래서 그대로 옮겨가는 것도 추가로 있어야함.
        elif  ordA in sett :
            answer+=cha
        elif ordA == ord('.') :# 마침표 연속 시 1개 남기고 지우기 /처음끝 체크하며  지우기
            if len(answer)==0: # 맨앞 점은 미사용 
                pass
            elif answer[-1]!='.':# dotal ==False:
                answer+='.'
                # dotal=True #  맨뒤점 (연속) 지우기는 아래에서 함
            continue
            
        # dotal=False
    #     print(answer)
    # print('111', answer)

    # 이미 위에서 answer의 직전값이 점 이면 점을 안 넣었기에, '연속 .'은 없음.
    # answer="aaa...."
    # m2) answer=answer.rstrip('.')
    for i in range(len(answer)): # 4단계 _끝(연속)점도 처리해주는 걸로 만들었었음.
        if answer[ -1 ]=='.':
            # print('i, -i-1, len(answer)',i, -i-1, len(answer))
            # print('222',answer)
            answer=answer[: -1]#- (i+1+1)  ]#len(answer)+1 -i-1 ]#-i-1]# len(answer)+1-i]# 1개 
            #; 이전 점에서 '한개씩' 빼야함. 이미 1개 빼서 저장한 거에다 또 증가한 i인덱스를 빼면 안됨
        else :
            break
    if len(answer)==0 :
        answer="a"

    elif len(answer) >=16 :
        answer=answer[:15] #not 16 # 0생각 # 저게 15개
        # answer=answer.rstrip('.')
        for i in range(len(answer)): 
            if answer[ -1 ]=='.':
                answer=answer[: -1]
                break
                
    if len(answer)<=2 :
        while(len(answer)<=2 ):
            answer+=answer[-1]        

        
    return answer
# : 1h 7m / 성능 +2 / 0.48ms -> 0.38ms -> 0.28ms -> 0.45ms # rstrip보다 내 알고리즘이 더 빠른 것 같았는데 운도 꽤 있나봄

# - 디버깅
# > rstrip('.') 직접구현 : 한 케이스에서 틀렸었음. 마지막꺼 한 개가 제거가 안됐었음.
# :; 뺄 때, 이미 한 개 빼서 저장한 거에다 또 증가한 i를 빼면 안됨#  이전 거에서 '한개씩' 빼야지. 

# - 다른 사람 코드
# > m_a~z한방에 가져오기 : set(string.ascii_lowercase)
# > m_한 방에 전부 소문자화 : str1.lower()
# > re.sub : 굳이? 
# : re.sub(pattern, replace, text) : text 중 pattern에 해당하는 부분을 replace로 대체한다. 

# [1] https://jjuha-dev.tistory.com/entry/Python-%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D-resub%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%B9%98%ED%99%98%ED%95%98%EA%B8%B0


