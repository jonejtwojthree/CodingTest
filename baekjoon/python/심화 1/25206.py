scores = [input().split() for _ in range(20)]

total_score = 0
total_hakjeom = 0
for _, hakjeom, grade in scores:
    score = 0
    if grade == "P":
        continue
    elif grade == "A+":
        score = 4.5
    elif grade == "A0":
        score = 4.0
    elif grade == "B+":
        score = 3.5
    elif grade == "B0":
        score = 3.0
    elif grade == "C+":
        score = 2.5
    elif grade == "C0":
        score = 2.0
    elif grade == "D+":
        score = 1.5
    elif grade == "D0":
        score = 1.0

    total_score += float(hakjeom) * score
    total_hakjeom += float(hakjeom)
print(round(total_score / total_hakjeom, 6))
