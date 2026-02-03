#wasaaaaa
from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)
no_clicks = 0

@app.route('/')
def index():
    return render_template('index.html', no_clicks=no_clicks)

@app.route('/yes')
def yes():
    global no_clicks
    no_clicks = 0
    return render_template('yes.html')

@app.route("/no")
def no():
    global no_clicks
    no_clicks += 1
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=50000)

