from flask import Flask

from admin.admin import admin as admin_blueprint
from front.front import front as front_blueprint

app = Flask(__name__)
app.register_blueprint(admin_blueprint,url_prefix = '/admin') # 注册蓝图
app.register_blueprint(front_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
