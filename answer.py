#Answer class
from datetime import datetime

class Answer:
    def __init__(self,answer):
        self.answer = answer
        self.timePosted = datetime.utcnow()

    def __repr__(self):
        return self.answer
