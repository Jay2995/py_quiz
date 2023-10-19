from question_model import Question;
from data import question_data;
from quiz_brain import Quiz_brain;

question_objects = [];

for question in question_data:
    text = question["text"];
    answer = question["answer"];
    questions = Question(text, answer);
    question_objects.append(questions);

quiz = Quiz_brain(question_objects)


while quiz.still_has_questions():
    quiz.next_question()
print(f"Your final score is {quiz.score}/{len(question_objects)}")