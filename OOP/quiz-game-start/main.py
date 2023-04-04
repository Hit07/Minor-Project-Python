from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
answer_bank = []
for q in question_data:
    new_question = Question(q["question"],q['correct_answer'])
    question_bank.append(new_question.text)
    answer_bank.append(new_question.answer)
# print(question_bank)
# print(answer_bank)

quiz_brain = QuizBrain(question_bank)
while quiz_brain.still_has_question():
    quiz_brain.next_question(answer_bank)
print(f"🎊You've Completed the Quiz!🎊\nYour Final Score:{quiz_brain.score}")