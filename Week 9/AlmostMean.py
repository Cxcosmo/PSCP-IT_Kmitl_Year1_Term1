"""AlmostMean"""
def main(n) :
    """AlmostMean"""
    student_list = []
    score_list = []
    sum_score = 0
    for _ in range(n) :
        score = input()
        sum_score += float((score.split())[1])
        student_list.append(score)
        score_list.append(float((score.split())[1]))
    average = sum_score / n
    sort_score = sorted(score_list)
    score_average = 0
    for i in sort_score :
        if i <= average :
            score_average = i
    find_index = score_list.index(score_average)
    print(student_list[find_index])
main(int(input()))
