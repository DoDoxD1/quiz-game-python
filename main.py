from question_model import Question
from data import question_data

question_bank = []

for question in question_data:
    ques = Question(question["text"], question["answer"])
    question_bank.append(ques)

for question in question_bank:
    print(f"Question: {question.text}")
