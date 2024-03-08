from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/list_prof/<list>')
def index(list):
    return render_template('base.html', list=list)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
