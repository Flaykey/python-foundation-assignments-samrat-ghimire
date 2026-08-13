student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}


for name , score in student_scores.items():
    print(name , score)

pass_dist = {name : score for name , score in student_scores.items() if score >= 60 }
print(pass_dist)

highest_score_name = ""
m = 0
for name , score in student_scores.items():
    if(score > m):
        m = score
        highest_score_name = name

print(highest_score_name)

average = 0
for score in student_scores.values():
    average += score

average /= len(student_scores)

print(average)