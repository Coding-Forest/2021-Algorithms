import numpy as np

def solution(citations):
    answer = 0
    total_cit = []

    for i in range(len(citations)):
        pubs = i+1
        cits = len([c for c in citations if (c >= pubs)])
        if (cits >= pubs):
            answer = cits

    return answer

solution([3, 0, 6, 1, 5])
