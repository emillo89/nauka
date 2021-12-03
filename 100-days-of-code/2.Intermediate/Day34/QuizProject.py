from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain
from ui import QuizInterface

'''question bank which consists of a list of question object'''
question_bank = []

for question in question_data:
    text = question['question']
    answer = question['correct_answer']
    new_question = Question(text,answer)
    question_bank.append(new_question)


print(question_bank)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

while quiz.still_has_question():
    quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final scire was: {quiz.score}/{len(question_bank)}")

