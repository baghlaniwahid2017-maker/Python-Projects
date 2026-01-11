


x = 10
score = [66, 90, 90, 90, 85]

def grade (ave):
    if ave > 90:
        return 'A'
    elif ave > 70:
        return 'B'
    elif ave > 55:
        return 'C'
    elif ave >= 50:
        return 'Pass'
    else:
        return 'Fail'

data = [66, 90, 90, 90, 85], [66, 90, 90, 90, 85], [70, 90, 85, 60, 85]

    
for x, scores in enumerate(data, start=1):
    avg = sum(scores) / len(scores)

print(f"Student {x}: Average = {avg:.2f}, Grade = {grade(avg)}")
    