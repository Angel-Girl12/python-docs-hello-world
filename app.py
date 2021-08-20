 # Sample.py
 
 from flask import Flask, render_template, url_for, request, redirect
 
 app = Flask(__name__)
 
 @app.route(\'/\')
 def hello_world():
     return \'hello,world\'

 @app.route(\'/user/<username>\', methods=[\'POST\', \'GET\'])
 def user(username):
     return \'Hello,%s\' % username
 
 @app.route(\'/user/login\')
 def login():
     return render_template(\'login.html\')
 
 @app.route(\'/user/redirect\', methods=[\'POST\'])
 def redirect_to_new_url():
     username = request.form[\'username\']
     return redirect(url_for(\'user\',username=username))
 
 if __name__ == \'__main__\':
     app.run(debug=True)
