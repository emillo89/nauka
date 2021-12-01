from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain

'''question bank which consists of a list of question object'''
question_bank = []

for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    question_bank.append(Question(text,answer))




quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final scire was: {quiz.score}/{len(question_bank)}")

