from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    answer_dict = {
        'title': 'Анкета',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True
    }
    return render_template('index.html', **answer_dict)




if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
