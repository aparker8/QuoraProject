from flask import Flask, request, jsonify
from flask.json import JSONEncoder

from question import Question
from answer import Answer

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Question):
            return {"question":obj.question,
            "timePosted":obj.timePosted}
        else:
            return super(MyJSONEncoder, self).defaut(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

questions = []

@app.route("/question", methods = ['POST'])
def hello():

    questions.append(Question(request.form['question']))

    return request.form['question']

@app.route("/questions")
def getQuestions():


    return jsonify(questions)


if __name__ == '__main__':
    app.run()



# question1 = Question("Why do humans have feet?")
# print question1
#
# question1.addAnswer("I unno")
# print question1
