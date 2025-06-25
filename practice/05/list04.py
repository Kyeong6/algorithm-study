"""
모의고사:
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려한다. 
- 1번 수포자: 1,2,3,4,5,1,2,3,4,5, ...
- 2번 수포자: 2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5, ...
- 3번 수포자: 3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5, ...
1번 문제부터 마지막 문제까지의 정답이 순서대로 저장된 배열 answers가 주어졌을 때
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 반환

제약조건:
1. 시험은 최대 10,000문제로 구성
2. 문제의 정답은 1,2,3,4,5 중 하나
3. 가장 높은 점수를 받은 사람이 여럿이라면 반환하는 값을 오름차순 정렬

분석:
- 문제에서 특정 값이나 패턴이 주어지면 해당 값을 "하드 코딩"하면 좋음
"""
def solution(answers):

    # 학습자들의 패턴
    patterns = [
        [1,2,3,4,5], # 1
        [2,1,2,3,2,4,2,5], # 2
        [3,3,1,1,2,2,4,4,5,5] # 3
    ]

    # 점수 저장
    scores = [0] * 3

    # 패턴과 정답 비교
    for i, answer in enumerate(answers):
        for j, patterns in enumerate(patterns):
            if answer == patterns[i % len(patterns)]:
                scores[j] += 1
    
    # 최고 점수
    max_score = max(scores)

    # 가장 높은 점수를 가진 수포자들의 번호 찾아서 리스트에 담음
    highest_scores =[]
    for i, score in enumerate(scores):
        if score == max_score:
            highest_scores.append(i+1)
    return highest_scores


answers = [1,2,3,4,5]