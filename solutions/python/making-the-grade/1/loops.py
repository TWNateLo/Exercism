"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """

    new_student_scores = []
    while student_scores:
        new_student_scores.append(round(student_scores[0]))
        student_scores.pop(0)
    return new_student_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    a = 0
    failed_count = 0
    while a < len(student_scores):
        if student_scores[a]<=40:
            failed_count += 1
        a += 1
    return failed_count

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    a = 0
    above_scores = []
    while (a < len(student_scores)):
        if student_scores[a] >= threshold:
            above_scores.append(student_scores[a])
        a += 1
    return above_scores
    
def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    gap = (highest - 40) // 4
    return [41, 41+gap, 41+gap*2, 41+gap*3]

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    """
    or doing the two enumerate at once with the zip() function:

    output = []
    for index, (name, score) in enumerate(zip(student_names, student_scores)):
        output.append(f"{index+1}. {name}: {score}")
    return output
    """

    output = []
    for index, name in enumerate(student_names):
        output.append(f"{index+1}. {name}: {student_scores[index]}")
    return output

def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    """ The all 100 version    
    perfect = []
    for a in range(len(student_info)):
        if student_info[a][1] == 100:
            perfect.append(student_info[a])
        else:
            continue
        
    return perfect
    """

    if student_info == []:
        return []
    else:
        for a in range(len(student_info)):
            if student_info[a][1] == 100:
                return student_info[a]
            elif a == len(student_info)-1:
                return []
            else:
                continue
    
