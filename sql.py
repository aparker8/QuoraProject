import sqlite3

conn = sqlite3.connect('quora.db')
c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")

c.execute("""CREATE TABLE IF NOT EXISTS Questions (
questionID integer PRIMARY KEY,
question text NOT NULL,
timePosted text NOT NULL default CURRENT_TIMESTAMP
)
""");


c.execute("""CREATE TABLE IF NOT EXISTS Answers (
questionID integer NOT NULL,
answerID integer PRIMARY KEY,
answer text NOT NULL,
timePosted text NOT NULL default CURRENT_TIMESTAMP,
UNIQUE (questionID, answerID),
FOREIGN KEY (questionID) REFERENCES Questions (questionID)
ON DELETE CASCADE
)
""");

c.execute("""INSERT INTO Questions (question)
VALUES ('What is your name?');
""")

c.execute("""INSERT INTO Questions (question)
VALUES ('What is your favorite color?');
""")

c.execute("""INSERT INTO Questions (question)
VALUES ('What is your quest?');
""")

def addQuestion(question):
    c.execute('INSERT INTO Questions (question) VALUES (?)',(question,))
    conn.commit()
    return c.lastrowid

def addAnswer(addQuestionID, answer):
    c.execute('INSERT INTO Answers (questionID, answer) VALUES (?, ?)',(addQuestionID, answer))
    conn.commit()

addQuestionID = addQuestion('What color is your parachute?')
addAnswer(1, 'Purple')

conn.commit()
