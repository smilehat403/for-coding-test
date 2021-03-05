import itertools
def solution(numbers):
    answer = ''
#     시원하게 싹다 시간초과 뜸!
#     max_num = 0    # 최댓값 변수는 작게 설정
#     # numbers에서 숫자(정수)를 꺼낸다음
#     # str으로 바꿔서 '6'+'10'+'2'한다음 다시 숫자로 바꿔서
#     # 여기서 조합말고 순열이 필요하다. 순열... 어떻게 써야하는지 까먹
#     # dfs로 가능할듯? def dfs(left:str,mid:str,right:str): 
#     # 문제!<- 10이 원소면 10을 써야하는데 1과 0을 씀...
#     # max_num = max(max_num, int(str(뭐시기)))로 할거임
#     # dfs하려고 한 흔적    >>>   # str_nums = ''.join(list(map(str,a)))
#                                 # half = len(str_nums)//2
#                                 # def(str_nums[:half],str_nums[half],str_nums[half+1:])
    
#     # numbers가 가지고 있는 int형 숫자를 str형으로 바꿔줘야함
#     str_nums = list(map(str,numbers))
#     # 1. 멍청하게 그냥 in str_nums함 / 2. permutation's'!!
#     for number in itertools.permutations(str_nums):
#         number = ''.join(number)            # permutations하면 tuple로 값이 나옴!
#         max_num = max(max_num,int(number))  # max비교할 때는 정수끼리
#     answer = str(max_num)
    
    # 어떻게 해야될까? 정렬을 가장 왼쪽 자리 기준으로 정렬한다음 싹 합쳐야함
    # numbers.sort(key = lambda:~~~) 근데 lambda를 잘 쓸 줄 모름 허허
    numbers = list(map(str,numbers))
    numbers.sort(key = lambda x: x*3,reverse = True)    # 진짜.... *3하는 아이디어는....후...
    # sorted(numbers, key = lambda x: x*3, reverse = True)
    # 왜 안되는지 한참 헤맸음.... tmp = sorted()
    # answer = ''.join(numbers)
    answer = str(int(''.join(numbers))) 
    # 진짜 미친 사람들인가... '0000'->'0' 노 어이...
    
    return answer