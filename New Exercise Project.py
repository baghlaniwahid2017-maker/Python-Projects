

# Student 5
# Subject 5

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

Students = [
    ("Ahmad", [66, 90, 90, 90, 85]),
    ]
     

    
for name, scores in Students:
     avg = sum(scores) / len(scores) 
print(f"{name}: Total = {sum(scores)}, Average = {avg:.2f}, Grade = {grade(avg)}")
    