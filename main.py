from flask import Flask, request, jsonify, abort, render_template
from flask.json import JSONEncoder

from question import Question
from answer import Answer

class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj,Question):
            return {"question":obj.question,
            "timePosted":obj.timePosted}
        elif isinstance(obj, Answer):
            return {"answer": obj.answer,
            "timePosted":obj.timePosted}
        else:
            return super(MyJSONEncoder, self).default(obj)

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

q = Question("Who dis?")
q.addAnswer("A-a-ron")


questions = [q]

@app.route("/question", methods = ['POST'])
def hello():

    questions.append(Question(request.form['question']))

    return request.form['question']

@app.route("/questions")
def getQuestions():

    return jsonify(questions)

@app.route("/answers/<int:questionID>")
def getAnswers(questionID):
    return jsonify(questions[questionID].answers)

@app.route('/<path:path>')
def get_file(path):
    if '..' in path or path.startswith("/"):
        abort(404)
    try:
        return app.send_static_file(path)
    except:
        return render_template(path, questions = questions)

if __name__ == '__main__':
    app.run()



# question1 = Question("Why do humans have feet?")
# print question1
#
# question1.addAnswer("I unno")
# print question1
