class QuizBrain:
    
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_position = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input("Q: {}: {} True or False: ".format(self.question_number, current_position.text))
        self.check_answer(user_answer, current_position.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print("Your score is: {}".format(self.score))
        else:
            print("You got it wrong!")
        print("Your current score is {}/{}\n".format(self.score, self.question_number))