from flask import Flask, render_template
from os import listdir, path


app = Flask(__name__)

PORTFOLIO_PATH = path.join(path.dirname(__file__), 'static/img/portfolio')


@app.route("/")
def hello():
    def compare(a, b):
        a_f = float(a[0])
        b_f = float(b[0])
        return (a_f > b_f) - (a_f < b_f)

    images = [(f.split('-'), path.join('img/portfolio', f))
              for f in listdir(PORTFOLIO_PATH)
              if path.isfile(path.join(PORTFOLIO_PATH, f))]
    images.sort(key=lambda i: float(i[0][0]))
    return render_template('index.html', images=images)
