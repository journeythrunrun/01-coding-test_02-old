# 가운데 글자 가져오기_https://school.programmers.co.kr/learn/courses/30/lessons/12903

# 길이_짝수 = 두글자 => 2) [4=>[1]&[2]] 3) leng//2-1 leng//2 
# _홀수 = 한글자   => 2) [5=>[3-1]] 3) leng//2
def solution(s): # len_O(1)
    return s[len(s)//2] if len(s)%2!=0 else s[len(s)//2-1:len(s)//2+1] 

# 해설[비슷]
# : 시복 동일_수학m->if문 제거_ 시복 동일*도아니고 -라 굳이 습득?
# return str[(len(str)-1)//2 : len(str)//2 + 1]
    