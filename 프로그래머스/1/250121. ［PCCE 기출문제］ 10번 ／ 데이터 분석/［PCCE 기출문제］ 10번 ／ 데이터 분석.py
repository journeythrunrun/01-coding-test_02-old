# 1)
# data의 각 행 : ["코드 번호(code)(1~)", "제조일(date)(20000101~)", "최대 수량(maximum)(1~)", "현재 수량(remain)(1~max)" ]
# -> 'ext <= val_ext'인 데이터만 뽑음
# sory_by 기준 오름차순 정렬 .sort (( ,key=lambda x:x[dict1[sort_by]]))

# 4) 정렬 기준에 해당하는 값이 서로 같은 경우는 없습니다.

# 2)
# m1 for 
# m2 ext, sort_by기준 미리 정렬 : 오히려 nlogn 
def solution(data, ext, val_ext, sort_by):
    answer = []
    dict1={"code":0, "date":1, "maximum":2, "remain":3 }
    print(dict1[ext])
    for i in range(len(data)):
        if data[i][dict1[ext]] <= val_ext : # target <= _ # -> 'ext <= val_ext'인 데이터만 뽑음
            answer.append(data[i])
    
    # sory_by 기준 오름차순 정렬
    answer.sort( key=lambda x:x[dict1[sort_by]]) # 기본이 오름차순
    return answer
# : 20m / 성능 +2 / 최대0.15ms

# - 딕셔너리를 거친 2단 인덱스

# - 다른 사람 풀이
# > 나_딕셔너리에 1대1 값 맵핑 <-> 리스트_내가 키로 사용한 것들 넣어놓고, .index(키)(-)로 정수 인덱스 사용 
# >> 물론 딕셔너리가 search 빨라서 쓰기 시작했던 것도 있지만 list 순차적&index법도 있음
# > 결과도 시작 data에 누적하며 저장 / 단지 압축식
# : 엄준식 = [엄 for 엄 in 엄준식 if 엄[어떻게사람이름이.index(준)]<식]

# def solution(엄준식, 준, 식, 준식):
#     어떻게사람이름이 = ["code","date","maximum","remain"]
#     엄준식 = [엄 for 엄 in 엄준식 if 엄[어떻게사람이름이.index(준)]<식]
#     엄준식.sort(key=lambda 엄: 엄[어떻게사람이름이.index(준식)])
#     return 엄준식
# [1] 코딩하는 엄준식