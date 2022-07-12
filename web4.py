from ast import If
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/index/<string:username>')
def index(username):
    user = 'amos'
    data = [1,'2,345','123455']
    userinfo = {'username':'amos','age':'18','email':'null'}
    return render_template('index.html', username=username,data = data,userinfo = userinfo)

if __name__ == '__main__':
    app.run(debug=True)