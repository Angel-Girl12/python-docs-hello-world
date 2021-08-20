# APP调试模式开关
DEBUG = True
 
'''
数据库配置
'''
# 数据库类型
SQL = 'mysql'
# 数据库驱动
DRIVER = 'pymysql'
# 数据库主机地址
HOST = '127.0.0.1'
# 数据库端口
PORT = 3306
# 数据库用户名
USERNAME = 'root'
# 数据库密码
PASSWORD = 'Angel0512'
# 数据库名
BASENAME = 'JOBDATA'
# 编码类型
CHARSET = 'utf8'
 
# 数据库配置最终变量内容
SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset={}" .format(SQL, DRIVER, USERNAME, PASSWORD, HOST, PORT, BASENAME, CHARSET)
 
SQLALCHEMY_TRACK_MODIFICATIONS = False
