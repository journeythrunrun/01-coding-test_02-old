# 카드 뭉치_https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 카드=길이1이상 / 영단어 적힘 / 서로 다른 단어 존재? 각각? 애매해서 굳이 신경 안 써도 되는 문제일듯

# 중복 불가. 카드 순서 사용.
def solution(cards1, cards2, goal):
    index1=0
    index2=0
    for a in goal:
        # '인덱스 체크' 'and' '인덱스 사용'# 파이썬 특이라 앞 False면 뒤 안함
        if index1<=len(cards1)-1 and a == cards1[index1] : # index =index error 체크
            index1+=1 
        elif  index2<=len(cards2)-1 and a== cards2[index2] :
            index2+=1
        else :
            return "No"
    return "Yes"

# - 해설[유사]
# - pop보다 <-> 나_index+1 접근이 계산.은 효율일듯. 메모리 까지하면 놉

    