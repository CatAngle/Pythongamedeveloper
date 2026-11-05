import random

# 1. Generate 20 random scores between 0 and 100
marks = [random.randint(0, 100) for _ in range(20)]

# 2. Initialize three empty lists
low_scores = []    # Scores <= 30
mid_scores = []    # Scores from 31 to 69
high_scores = []   # Scores >= 70

# 3. Iterate through the scores and classify them
for mark in marks:
    if mark <= 30:
        low_scores.append(mark)
    elif 31 <= mark <= 69:
        mid_scores.append(mark)
    else:  # mark >= 70
        high_scores.append(mark)

# 4. Display the results
print(f"Original 20 generated scores: {marks}")
print("-" * 40)
print(f"List 1 (scores <= 30): {low_scores}")
print(f"List 2 (scores 31-69): {mid_scores}")
print(f"List 3 (scores >= 70): {high_scores}")