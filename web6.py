from flask import Flask,render_template ,request
from requests import session

app = Flask(__name__)
app.config['SECURET_KEY'] = 'qweqfqfd'

@app.route('/')
def index():
    if not session.get('user'):
        return redirect(url_for('login'))


    return render_template('index.html')


@app.route('/login',methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == "" and password == "":
            return "login success"
        else:
            return "login failed"

    

app.run(debug=True)