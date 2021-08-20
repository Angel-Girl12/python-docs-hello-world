from exts import db
 
# user表模型类
class user(db.Model):
    # 操作的表名称
    __tablename__ = 'JOBtbl'
 
    # 字段信息
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
