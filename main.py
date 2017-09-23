from flask import Flask, request, jsonify

from question import Question
from answer import Answer

app = Flask(__name__)

questions = []

@app.route("/question", methods = ['POST'])
def hello():

    questions.append(Question(request.form['question']))

    return request.form['question']

@app.route("/questions")
def getQuestions():

    response = {}

    for i, question in enumerate(questions):
        response[i] = {

        "question": question.question,
        "timePosted": question.timePosted
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run()



# question1 = Question("Why do humans have feet?")
# print question1
#
# question1.addAnswer("I unno")
# print question1
