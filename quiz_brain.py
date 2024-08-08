class QuizBrain:
    def __init__(self, questions):
        self.questions_list = questions
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.questions_list)

    def next_question(self):
        question = self.questions_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q.{self.question_number} {question.text} (True/False)?: ")
        self.check_answer(ans, question.answer)

    def check_answer(self, ans, answer):
        if answer == ans:
            self.score += 1
            print("You got it right!")
        else:
            print("That was not correct")
        print(f"The correct answer was {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
