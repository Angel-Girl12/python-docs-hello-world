from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = '84375r0hfuggwkjvgfjhvsjhgv'


# 数据库连接
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1:3306/bookmanager'
# 动态追踪修改设置，如未设置只会提示警告
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# 查询时会显示原始SQL语句
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


class Admin(db.Model):
    __tablename__ = 'admin'
    id = db.Column(db.Integer,primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    pwd = db.Column(db.String(128), nullable=False)


@app.route('/init')
def init():
    # db.create_all()
    return 'ok'


@app.route('/admin/register', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user = request.form.get('user')
        pwd1 = request.form.get('pwd1')
        pwd2 = request.form.get('pwd2')
        if all([user, pwd1, pwd2]):
            if pwd1 == pwd2:
                a = Admin()
                a.user = user
                a.pwd = pwd1
                db.session.add(a)
                db.session.commit()
                flash('注册成功')
            else:
                flash('两次密码输入不一致')
        else:
            flash('输入信息不全')
    return render_template('admin/register.html')
# request 从请求里读内容


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if all([user, pwd]):
            a = Admin.query.filter(Admin.user == user).first()
            if a:
                # 如果用户存在，判断密码是否正确
                if a.pwd == pwd:
                    # 登录成功后，session['admin_id']存入数据，
                    # 其他页面用来判断用户到登录状态
                    session['admin_id'] = a.id
                    flash('登陆成功')
                    # 登录成功后跳转到首页，对图书进行管理
                    return redirect(url_for('ind'))
                else:
                    flash('密码错误')
            else:
                flash('用户名不存在')
        else:
            flash('用户名、密码不完整')
    return render_template('admin/login.html')


@app.route('/user')
def ind():
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
© 2021 GitHub, Inc.