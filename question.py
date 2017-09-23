#Question class
from datetime import datetime

from answer import Answer

class Question:
    def __init__(self,question):
        self.question = question
        self.answers = []
        self.timePosted = datetime.utcnow()

    def __repr__(self):
        return "Question:" + self.question + ", Answers:" + str(self.answers)

    def addAnswer(self, answer):
        self.answers.append(Answer(answer))
