from question_model import Question
from data import question_data

'''question bank which consists of a list of question object'''
question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    question_bank.append(Question(text,answer))


quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()