from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof):
    return render_template('index.html', prof=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
