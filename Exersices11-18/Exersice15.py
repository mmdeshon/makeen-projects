def mean_scores(scores_dict):
    count = 0
    starter = 0
    for score in scores_dict.values():
        starter += score
        count += 1
    return starter / count


scores = {"Mathematics": 18, "History": 16, "Physics": 20}
print(mean_scores(scores))