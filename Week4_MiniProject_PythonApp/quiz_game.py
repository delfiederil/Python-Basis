# Simple Quiz Game

questions = {
    "What is Python?": "programming language",
    "Who developed Python?": "Guido van Rossum",
    "Python is interpreted or compiled?": "interpreted"
}

score = 0
for q, ans in questions.items():
    user_answer = input(q + " ")
    if user_answer.strip().lower() == ans.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Answer: {ans}")

print(f"Your score: {score}/{len(questions)}")
