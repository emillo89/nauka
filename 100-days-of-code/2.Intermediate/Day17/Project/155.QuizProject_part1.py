from question_model import Question
from data import question_data

'''question bank which consists of a list of question object'''
question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    question_bank.append(Question(text,answer))




print(question_bank[0].text)