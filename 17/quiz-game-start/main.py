from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))

test = QuizBrain(question_bank)
while test.still_has_questions():
    test.next_question()

print("You've completed the quiz.")
print(f"Your final score was : {test.score}/{test.question_number}")