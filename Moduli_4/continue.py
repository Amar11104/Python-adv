scores = [68,42,57,78,35,62,50,92]

total = 0
count = 0

for score in scores:
    if score < 50:
        total += score
        count += 1

avg = total / count if count > 0 else 0

print("avg score for scores above 50: ", avg)










