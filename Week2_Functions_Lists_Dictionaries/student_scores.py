# Store student scores in a dictionary
scores = {"Alice": 90, "Bob": 80, "Charlie": 85}

# Function to display scores
def display_scores(data):
    for name, mark in data.items():
        print(f"{name}: {mark}")

display_scores(scores)
