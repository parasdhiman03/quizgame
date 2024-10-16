def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

    answer = input("Your answer (A, B, C, or D): ").upper()
    while answer not in ['A', 'B', 'C', 'D']:
        answer = input("Invalid input. Please enter A, B, C, or D: ").upper()

    return answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}.\n")
        return False


def run_quiz(quiz_data):
    score = 0
    for question_data in quiz_data:
        user_answer = ask_question(question_data)
        if check_answer(user_answer, question_data["correct_answer"]):
            score += 1
    print(f"Quiz Over! Your final score is {score}/{len(quiz_data)}.")
