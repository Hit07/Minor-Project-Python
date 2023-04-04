# TODO: Asking the questions
# TODO: Checking if the answer was correct
# TODO: Checking if we are the end of the quiz
class QuizBrain:
    """Create a class called QuizBrain.
       Write an __init__() method
       Initialise the question_number to 0
       Initialise the question_list to an input"""
    def __init__(self,question_list):
        """Initialises all the variables to the starting values and inputs the questions"""
        self.question_number = 0
        self.answer_number = 0
        self.q_list = question_list
        self.score = 0
    def still_has_question(self):
        """Checks if there is still any questions in question bank and returns true if yes or false"""
        return self.question_number<len(self.q_list)

    def next_question(self,answer_bank):
        '''Retrieves the question from the current question  number and prompts the user
           for his answer'''
        self.answer_bank = answer_bank
        question = self.q_list[self.question_number]
        self.question_number += 1
        input_1 = input(f"Q.{self.question_number}.{question} (True/False): ").title()
        if input_1 == self.answer_bank[self.answer_number]:
            self.score += 1
            print(f"You got it right!!👏\nCorrect answer: {self.answer_bank[self.answer_number]}\n{self.score}/{len(self.q_list)}")
            self.answer_number += 1
        else:
            print(f"Wrong answer!!😓\nCorrect answer: {self.answer_bank[self.answer_number]}\n{self.score}/{len(self.q_list)}")
            self.answer_number += 1


