class QuizBrain():

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        question = self.question_list[self.question_number].text
        answer_list = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} : {question} (True or False): ")
        self.check_answer(user_answer, answer_list)


    def check_answer(self, user_answer, answer):
        if user_answer.lower() == answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print("That's wrong")
        print(f"The correct answer was: {answer}")
        print(f"The current score is : {self.score} / {self.question_number}")
        print("\n")





