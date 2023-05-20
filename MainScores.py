import os
from flask import Flask
from flask import render_template

# instance of flask application
app = Flask(__name__)


@app.route("/score_server")
def score_server():
    try:
        document_path = os.getcwd() + '/app/Scores.txt'
        with open(document_path, mode='r', encoding='utf-8') as scores_file:
            score = scores_file.readline()
            return render_template('ScoresGame.html', SCORE=score)
    except BaseException as e:
        return render_template('ScoresGame.html', ERROR=e)

#
# @app.route("/register")
# def register():
#     document_path = os.getcwd() + '/hello.txt'
#     words_file = open(document_path, mode='a', encoding='utf-8')
#
#     words_file.write('hello');
#
#     return 'Hello', 201;


if __name__ == '__main__':
    # app.run(debug=True, port=30000)
    app.run(host='0.0.0.0')
