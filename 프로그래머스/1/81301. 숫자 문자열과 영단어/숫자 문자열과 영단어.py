#숫자 문자열과 영단어_https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 문자열 단어 -> 숫자
# ( s= 안 빔, 결과=자연수 )

#_	통과 (0.03ms, 10.4MB)
def solution(str1):
    # upper() lo
    answer=''
    i=0
    while(i<=len(str1)-1):

        if str1[i].islower() : # 소문자
            if str1[i]=='z':
                answer+='0'
                i+=1+3
                continue
            elif str1[i]=='o':
                answer+='1'
                i+=1+2
                continue
            elif str1[i:i+2]=='tw':
                answer+='2'
                i+=1+2
                continue
            elif str1[i:i+2]=='th':
                answer+='3'
                i+=5
                continue
            elif str1[i:i+2]=='fo':
                answer+='4'
                i+=4
                continue
            elif str1[i:i+2]=='fi':
                answer+='5'
                i+=4
                continue
            elif str1[i:i+2]=='si':
                answer+='6'
                i+=3
                continue
            elif str1[i:i+2]=='se':
                answer+='7'
                i+=5
                continue
            elif str1[i]=='e':
                answer+='8'
                i+=5
                continue
            elif str1[i]=='n':
                answer+='9'
                i+=4
                continue
        else:
            answer+=str1[i]
            i+=1
            
    return int(answer)
# 해설- str1.replace()
# num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

# def solution(s):
#     answer = s
#     for key, value in num_dic.items():
#         answer = answer.replace(key, value)
#     return int(answer)
                
            

        

    