def calculate_percentage(score, total):
    return (score / total) * 100


# Step 1: Questions setup
quiz = [
    {
        "question": "What is the capital of Nigeria?",
        "options": ["A. Lagos", "B. Abuja", "C. Kano", "D. Ibadan"],
        "correct_answer": "B"
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["A. Python", "B. HTML", "C. Java", "D. All of the above"],
        "correct_answer": "D"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Computer Personal Unit", "C. Central Power Unit", "D. Control Processing Unit"],
        "correct_answer": "A"
    }
]


# Step 2: Loop through questions
score = 0

print("=== Welcome to the CLI Quiz ===\n")

for i, q in enumerate(quiz, start=1):
    print(f"Question {i}: {q['question']}")

    for option in q["options"]:
        print(option)

    # Step 3: Get user input
    answer = input("Enter your answer (A/B/C/D): ").upper()

    # Step 4: Check answer
    if answer == q["correct_answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer is {q['correct_answer']}\n")


# Step 5: Final result
total_questions = len(quiz)
percentage = calculate_percentage(score, total_questions)

print("=== Quiz Completed ===")
print(f"Your Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 50:
    print("🎉 You Passed!")
else:
    print("😢 You Failed!")