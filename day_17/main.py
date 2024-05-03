import data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q in data.question_data:
    question_bank.append(Question(q["text"], q["answer"]))

quiz = QuizBrain(question_bank)

while QuizBrain.more_questions(quiz):
    QuizBrain.next_question(quiz)

print()
print("You have completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
