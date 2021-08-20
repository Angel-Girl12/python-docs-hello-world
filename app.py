from flask import Flask, request, url_for, redirect, render_template, session
from exts import db
from models import user
import os,config
 
# 实例化flask
app = Flask(__name__)
 
# 将config文件作为配置
app.config.from_object(configs)
 
# 初始化db
db.init_app(app)
 
@app.route('/')
def index():
    # 赋值session
    session['userinfo'] = {'name': '张三'}
 
    # 数据库查询测试
    res = user.query.filter(user.id==1).all()
    list_res = {}
    # 遍历结果集
    for i in res:
        # 打印结果
        print(str(i.id) + '----' + i.name + '---' + str(i.age))
    return '处理完成'
 
 
# 注册路由
@app.route('/user/<id>', methods=['GET', 'POST'])
def getuserId(id):
    # 转换数据类型
    id = int(id)
    # 判断请求类型测试
    if request.method == 'POST':
        return 'post info'
    else:
        if id == 1:
            # 重定向跳转测试
            return redirect('http://www.baidu.com')
 
        elif id == 2:
            # 渲染指定模板测试
            return render_template('test.html', name='张三')
 
        elif id == 3:
            # 判断session是否存在
            if 'userinfo' in session:
                return 'you login success,username:' + session['userinfo']['name']
            else:
                # 重定向，反向url生成
                return redirect(url_for('index'))
 
        else:
            # 得到动态参数
            return 'userId:' + str(id)
 
 
if __name__ == '__main__':
    # 生成session秘钥
    app.secret_key = os.urandom(10)
    # 运行服务，这里host是指绑定所有本地ip，port是绑定的端口
    app.run(host='0.0.0.0', port=80)
