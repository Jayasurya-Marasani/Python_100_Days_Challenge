student_scores = [180, 124, 165, 173, 189, 169, 146]

print(sum(student_scores))
total = 0
for score in student_scores:
    total += score

print(total)

print(max(student_scores))
max_score = student_scores[0] 
for score in student_scores:
    if score>max_score:
        max_score = score

print(max_score)


