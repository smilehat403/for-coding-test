# https://ilovemymoments.tistory.com/26 참고 내가 좋아하는 코드
answer = 0


def dfs(now_word, target, words, visited):
    global answer
    stacks = [now_word]

    while stacks:
        now = stacks.pop()
        if now == target:
            return answer

        for idx, word in enumerate(words):
            if _get_diff(now, word) == 1:
                if visited[idx] == 1:
                    continue
                visited[idx] = 1
                stacks.append(word)
        answer += 1


# zip을 사용하기 위해서는 word1과 word2가 무조건 같다는 보장이 있어야함
def _get_diff(word1, word2):
    return sum([i != j for i, j in zip(word1, word2)])


def solution(begin, target, words):
    global answer

    # 이게 return 0을 보장해주나? 만약 target이 words안에 있는데
    # 연결고리가 끊어진 경우는 어떡하지?
    if target not in words:
        return 0

    visited = [0] * len(words)
    dfs(begin, target, words, visited)

    return answer

begin = "hit";target = "cog"; words = ["hot", "dot", "dog", "lot", "log", "cog"]
solution(begin,target,words)