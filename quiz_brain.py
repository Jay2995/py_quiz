

class Quiz_brain():
    def __init__(self, q_list):
        self.question_number = 0;
        self.question_list = q_list;
        self.score = 0;
    def still_has_questions(self):
        if self.question_number > len(self.question_list):
            return False;
        elif self.question_number < len(self.question_list):
            return True;

    def next_question(self):
        current_question = self.question_list[self.question_number];
        self.question_number += 1;
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/False :)").lower();
        self.check_answer(answer, current_question.answer)


    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1;
            print("Correct Answer")
        elif user_answer != correct_answer.lower():
            print("Incorrect answer")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
        




