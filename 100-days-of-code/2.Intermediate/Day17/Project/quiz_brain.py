class QuizBrain():

    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list


    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        answer = self.question_list[self.question_number].text
        self.question_number += 1
        input(f"Q{self.question_number} : {answer} (True or False)")






