from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
# 独立的文件引入db是为了models.py和app.py引入不冲突，不然会导致循环引入
