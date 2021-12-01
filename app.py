from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from werkzeug import exceptions

app = Flask(__name__)
app.config['SECRET_KEY'] = '5204956a60384b5685e8ce01e34235517b576fc6a461ff13'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class UrlModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(250), unique=True, nullable=False)
    url_short = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"UrlModel('{self.url}', '{self.url_short}')"

def find_url(url):
    found = UrlModel.query.filter_by(url=url).first()
    print(found)
    return found


def find_short(short):
    found = UrlModel.query.filter_by(url_short=short).first()
    print(found)
    return found


def isValid(id):
    if len(id) != 7:
        return False
    else:
        return True

@app.route('/')
def home():
    return render_template('home.html', title='home')

@app.route('/prediction', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        print(request.form)
        piece_count = request.form['piece_count']
        result = pricer.predict(piece_count)
        return render_template('predict.html', default=piece_count, result=result)
    else:
        return render_template('predict.html', default=0, result=0, title='Predict')

@app.route('/reminder', methods=['GET', 'POST'])
def reminder():
    piece_count = request.form['piece_count']
    result = request.form['result']
    to_email = request.form['to_email']
    msg = Message("Your LegOh! prediction is here!", sender="futureproof.testing@gmail.com", recipients=[to_email])
    msg.html = render_template('mailers/your_result.html', piece_count=piece_count, result=result)
    # mail.send(msg)
    return render_template('thankyou.html')


@app.errorhandler(exceptions.BadRequest)
def handle_405(err):
    return render_template('errors/405.html')

@app.errorhandler(404)
def handle_400(err):
    return render_template('errors/404.html')

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return render_template('errors/500.html')


if __name__ == '__main__':
    app.run(debug=True)
