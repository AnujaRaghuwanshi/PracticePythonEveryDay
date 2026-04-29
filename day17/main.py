from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
    question_text = data["question"]
    answer = data["correct_answer"]
    question_bank.append(Question(question_text, answer))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score}/ {len(question_bank)}")

