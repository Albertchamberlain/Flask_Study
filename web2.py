from flask import Flask ,render_template #导入Flask类和render_template函数渲染一个模板
from sympy import appellf1

app = Flask(__name__,template_folder="views") #创建一个Flask对象

@app.route('/')
def index():
    html = open('views/index.html').read()
    return  html


@app.route('/template')
def template():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
