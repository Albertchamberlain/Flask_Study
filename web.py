from flask import Flask
import uuid
app = Flask(__name__)

@app.route('/index')
@app.route('/')
@app.route('/index2')
def index():
    return '<h1>index page/h1>'


@app.route('/home/<string:username>')
def home(username):
    print(username)
    return '<h1>home page/h1>'

@app.route('/home/<int:userid>')
def home2(userid):
    print(userid,type(userid))
    return '<h1>home page/h1>'

@app.route('/home/<float:userid>')
def home3(userid):
    print(userid,type(userid))
    return '<h1>home page/h1>'

@app.route('/home/<path:userid>') #path可以接受任意字符串 带/的字符串
def home4(userid):
    print(userid,type(userid))
    print(uuid.uuid4.__str__)
    return '<h1>home page/h1>'

@app.route('/home/<uuid:userid>') #uuid可以接受uuid格式的字符串
def  home5(userid):
    print(userid,type(userid))
    return '<h1>home page/h1>'

@app.route('/home/<int:userid>/<string:username>')#可以接受多个参数
def home6(userid,username):
    print(userid,type(userid))
    print(username,type(username))
    return '<h1>home page/h1>'

#2.
def about(userid):
    return "about page" % userid
app.add_url_rule(rule='/about/<int:usreid>',view_func=about,endpoint='about')

if __name__ == '__main__':
    app.run(debug=True)