import itertools

def prime_table(num_size:int,primes:list):
    nums = [False,False]+[True]*(num_size-1)
    for num in range(2,num_size+1):
        if nums[num]:
            primes.append(num)
        for mult_num in range(num*2,num_size+1,num):
            nums[mult_num] = False
    

def solution(numbers:str):
    answer = 0
    list_num = [s for s in numbers]
    num_size = int(''.join(sorted(numbers,reverse=True))); primes = []
    prime_table(num_size,primes)    # prime_tabel update
    
    # permutation 함수를 어떻게 사용할 수 있나?
    # pool = ['A', 'B', 'C']
    # print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
    # print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
    rm_overlap = set() 
    for many_num in range(1,len(list_num)+1):
                                              # permutation's'임 + list_num은 문자열이어야 함
        for comb in list(map(''.join, itertools.permutations(list_num,many_num))): # for~~ : 안붙임
            rm_overlap.add(int(comb))
            
    for value in rm_overlap:
        if int(value) in primes:
            answer += 1

    return answer