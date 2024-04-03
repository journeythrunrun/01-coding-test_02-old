#[1차] 비밀지도_https://school.programmers.co.kr/learn/courses/30/lessons/17681
# 한 변 n / 1=벽_ or, 0=공백_and
# 원소 0인 case

# 통과 (0.38ms, 10.2MB)
# met_함수 따로 빼기 : 시복 줄이려할 때는 한 번에 보기/수정 불편한듯. 그래도 재귀함수 등은 가능
def to_two(a,b,n): # 1 line
    ans=''
    #reverse.
    for i in range(n-1,-1,-1): # n ##
        # old값 저장하기보다 간단 연산이니 한번에.
        # 앞큰값 버린 값에서, 몫구하기
        aa=  a%(2**(i+1) ) //(2**(i)) # c & 없으면 0  # 'a'+""""""3
        bb=b%(2**(i+1) ) //(2**(i)) 
        
        ans += '#' if aa or bb else " "
    return ans

def solution(n, arr1, arr2):
    # 2진수로.
    # 2] x=a*2^0 + b*2^1 + c*2^2 #3
    lines=[]
    for i in range(len(arr1)):
        lines.append(to_two(arr1[i], arr2[i],n )) #'11111' #시복단축 
    # m_s) 자릿수에 대한의미로 9,20 등에서 연산계산을 통해 바로 출력해보려하다가 생각하는데 시간 걸릴 것 같아서 패쓰
    return lines

# 해설_훨빠름 _ 진수변환함수사용_나머진 시복 비슷.< - > 나_k진수변환 직접 구현
# - 2진수로는 bin, 10진수로는 int
# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str( bin(i|j)[2:]  )
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer