from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/index/<string:username>')
def index(username):
    return '<h1>hello %s</h1>' % username


@app.route('/home')
def home():
    print(url_for('/index'))
    return redirect(url_for('index',username='amos'))


if __name__ == '__main__':
    app.run(debug=True)