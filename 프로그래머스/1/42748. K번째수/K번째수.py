#K번째수_https://school.programmers.co.kr/learn/courses/30/lessons/42748

####m효율 어차피 정렬할것(굳이 안함)
# 자르고, 정렬, k번째 수 
# 두 입력 안 빔, 입력1_자연수 

# '번째' < -> 'index' 주의. 
# 저장도안된 리스트슬라이싱.sort()처럼 막 연속기도 안됨
def solution(array, commands):
    answer=[]
    for i in range(len(commands)):
        temp=sorted(array[commands[i][0]-1:commands[i][1]+1-1])    
        answer.append(temp[commands[i][2] -1] )
        
    return answer
    # 비자연수~/ n번쨰 숫자가 인덱스 초과 / 너무 어거지? -> 이 정도는 처리 안 해도 맞음 항상.
    
    