# DFS 밖에 생각이 안났다. 근데 그러면 최대 5^8인데 사실 이게 시간초과 뜰지 안뜰지 잘 모르겠다
# 일단 DFS로 구현한번 해보려고 노력 
# +ㅁ+ㅁ+ㅁ+ㅁ+ㅁ+ㅁ+ㅁ+ㅁ 이렇게 될텐데... 저기 +자리에 사칙연산+숫자 합치기를 다 넣어볼 생각
# 왜 DP인지 모르겠다
# dfs로 하려고 했으나 연산 순서 때문에 실패함 -> 5+5+(5/5) 같은 경우...... (5+5+5)/5로 처리
# 결국 찾아봄.... 지렸음....... dp라니

def solution(N, number):
    answer = 0
    # 5 1개로 만들 수 있는 수 -> 5
    # 5 2개로 만들 수 있는 수 -> 10 0 25 1 55   -> 어떻게 합칠까?
    # 중복을 없애기 위해 set을 이용. set의 index+1은 N의 갯수를 의미
    numset = [set() for _ in range(8)]      # [set(), set(), set(), set(), set(), set(), set(), set()]
    for i,x in enumerate(numset,start = 1): # i가 1부터 시작
        x.add(int(str(N)*i))                # str(N)*i를 이용해서 숫자를 합치는 거 -> 미쳤음 아이디어
                                            # [{5}, {55}, {555}, {5555}, {55555}, {555555}, {5555555}, {55555555}]
    # {55} -> {10, 0, 25, 1, 55}로 변신시켜야함
    # for num1 in numset[0]:
    #     for num2 in numset[0]:
    #         numset[1].add(num1+num2)
    #         numset[1].add(num1-num2)
    #         numset[1].add(num1*num2)
    #         if num2 :                       # 0일때 예외처리.... 아오
    #             numset[1].add(num1//num2)   # 소수점 무시
    #
    # {555} -> {}은 (numset[0],numset[1])U(numset[1],numset[0]) 순서에 영향 받음
    #
    # for num1 in numset[1]:
    #     for num2 in numset[0]:
    #
    # for num1 in numset[0]:
    #     for num2 in numset[1]:
    
    for i in range(1,8):                      # 숫자 사용 갯수
        for j in range(i):                    # 사용 갯수 index
            for num1 in numset[j]:
                for num2 in numset[i-j-1]:
                    numset[i].add(num1+num2)
                    numset[i].add(num1-num2)
                    numset[i].add(num1*num2)
                    if num2 :                       # 0일때 예외처리.... 아오
                        numset[i].add(num1//num2)   # 소수점 무시
    
    for i,x in enumerate(numset,start=1):
        if number in x:
            answer = i
            return answer
    
    answer = -1     # 8번 안에 없다는 뜻 -> -1    
    
    return answer