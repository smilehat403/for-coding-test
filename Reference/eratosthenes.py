num_size = 1000
nums = [False,False]+[True]*(num_size-1)
primes = []

for num in range(2,num_size+1):
  if nums[num]:
    primes.append(num)
  for mult_num in range(num*2,num_size+1,num):
    nums[mult_num] = False

print(primes)
