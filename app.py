# Sample.py
 2 
 3 from flask import Flask, render_template, url_for, request, redirect
 4 
 5 app = Flask(__name__)
 6 
 7 @app.route(\'/\')
 8 def hello_world():
 9     return \'hello,world\'
10 
11 @app.route(\'/user/<username>\', methods=[\'POST\', \'GET\'])
12 def user(username):
13     return \'Hello,%s\' % username
14 
15 @app.route(\'/user/login\')
16 def login():
17     return render_template(\'login.html\')
18 
19 @app.route(\'/user/redirect\', methods=[\'POST\'])
20 def redirect_to_new_url():
21     username = request.form[\'username\']
22     return redirect(url_for(\'user\',username=username))
23 
24 if __name__ == \'__main__\':
25     app.run(debug=True)
