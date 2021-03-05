################ mine ################
def solution(participant, completion):
    answer = ''
    participant.sort(); completion.sort()
    for i in range(len(completion)):
        if participant[i] == completion[i]:
            continue
        else:
            answer = participant[i]
            return answer
    return participant[-1]


################## answer ##################
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

################## counter #################
from collections import Counter

Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})