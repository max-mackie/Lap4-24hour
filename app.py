from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from form import UrlForm
import shortuuid
from werkzeug import exceptions


app = Flask(__name__)
app.config['SECRET_KEY'] = '5204956a60384b5685e8ce01e34235517b576fc6a461ff13'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
    if len(id) != 6:
        return False
    else:
        return True

@app.route('/')
def home():
    return render_template('home.html', title='home')

@app.route("/short", methods=['GET', 'POST'])
def short():
    form = UrlForm()
    if request.method == 'POST':
        if find_url(form.url.data):
            found_url = find_url(form.url.data).url
            found_short = find_url(form.url.data).url_short
            return render_template('result.html', url=found_url, url_short=found_short)
        else:
            short = shortuuid.uuid()[:6]
            url = UrlModel(url=form.url.data, url_short=short)
            db.session.add(url)
            db.session.commit()
            return render_template('result.html', url=url.url, url_short=short)
    else:
        return render_template('short.html', form=form)

@app.route("/<string:id>")
def change(id):
    if isValid(id):
        url = find_short(id).url
        return redirect(url)
    else:
        return render_template('404.html')

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
