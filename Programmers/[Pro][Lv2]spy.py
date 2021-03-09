def solution(clothes):
    answer = 1
    # [["face"칸],["eyewear칸"].["headgear칸"]] 이렇게 만들 수는 없을까?
    # 그 다음 각 칸에 "0"을 추가해준다. 안입는 경우
    # 그 다음 모든 칸의 길이를 곱한다음 -1(아예 안입는 경우)를 빼주고 싶다
    cloth_type = set()
    for elem in clothes:
        cloth_type.add(elem[-1])     
    # 각 type에 번호를 부여해야 index를 얻을 수 있다. -> dict으로 만들자
    type_idx = {cloth[-1]:0 for cloth in clothes}   # {"face": 0, "eyewear":0 ...} 이렇게
    idx = 0
    for ct in cloth_type:                           # cloth_type에 옷종류가 다 있음
        type_idx[ct] += idx                         # idx 0,1,2,3,4...이렇게 증가
        idx += 1                                    # {"face": 0, "eyewear":1 ...}
    
    classify = [["0"] for _ in range(len(cloth_type))]     # ["0"]*3 -> ["0","0","0"]
    for wear, ct in clothes:
        classify[type_idx[ct]].append(wear)         # type_idx["face"]에 해당하는 인덱스의 classify에 추가해줌
                                                    # ["0","crowmask"]["0"]["0"]["0"]["0"]["0"] 이렇게 될거임
    
    for i in range(len(classify)):
        answer *= len(classify[i])                  # classify 모든 행렬들의 크기(=옷의 종류, 안입는 경우 포함)를 곱함
    
    answer -= 1                                     # 아예 안입는 경우 제거
    
    return answer



########### 자살 마려운... 깔끔한 풀이 ###########
def solution(clothes):
  from collections import Counter
  from functools import reduce
  cnt = Counter([kind for name, kind in clothes])
  answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
  return answer