def solution(numbers, target):
  # numbers[0]을 꺼낸다음 target에 계속 빼주는 형태.
  if not numbers and target == 0:
    return 1 
  elif not numbers:
    return 0
  else:
    return soultion(numbers[1:],target-numbers[0]) + soultion(numbers[1:],target+numbers[0])