# Function to calculate average score
def average_score(data):
    return sum(data.values()) / len(data)

scores = {"Alice": 90, "Bob": 80, "Charlie": 85}
print("Average Score:", average_score(scores))
