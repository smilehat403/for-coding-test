import collections


def solution(a):
    answer = -1
    if len(a) <= 1:
        return 0
    # preprocessor
    idx = 1
    while idx < len(a) - 1:
        if (a[idx - 1] == a[idx]) and (a[idx] == a[idx + 1]):
            del a[idx]
        else:
            idx += 1
    if (a[0] == a[1]):
        del a[0]
    if (a[-2] == a[-1]):
        del a[-1]
    # a의 전처리 끝, a의 most는 의미 있는 수
    if len(a) <= 1:
        return 0
    after = collections.Counter(a).most_common()
    most_num = after[0][0]
    # 그리디로 most_num보일때마다 제거하자
    tmp = []
    i = len(a) - 1
    while i >= 1:
        if a[i] == most_num and a[i-1]!=most_num:
            tmp.append(a[i])
            tmp.append(a[i - 1])
            i -= 2
        elif a[i-1] == most_num and a[i]!=most_num:
            tmp.append(a[i])
            tmp.append(a[i - 1])
            i -= 2
        else:
            i -= 1
    answer = len(tmp)

    return answer