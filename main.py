from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('user_signup_form.html', title="Signup Form")

def isblank(field):
    if field == '':
        return True
    else:
        return False
    
@app.route('/register', methods=['POST'])
def validate():
    #get form values and store as local variables
    username = request.form['username']
    password = request.form['password']
    verpassword = request.form['verpassword']
    email = request.form['email']
    
    #create blank error messages
    username_error = ''
    password_error = ''
    verpassword_error = ''
    email_error = ''
    
    if isblank(username):
        username_error = 'Username field must not be blank'
        #return render_template('user_signup_form.html',username_error=username_error, title="Error")
    if isblank(password):
        password_error = 'Password field must not be blank'
        #return render_template('user_signup_form.html',password_error=password_error, title="Error")
    if isblank(verpassword):
        verpassword_error = 'Verify Password field must not be blank'
    elif password != verpassword:
        verpassword_error = 'Verify Password must match Password'
        password = ''
        verpassword = ''
        
    if username_error or password_error or verpassword_error or email_error:
        return render_template('user_signup_form.html',username=username,
                           password=password,
                           verpassword=verpassword,
                           email=email,
                           username_error=username_error, 
                           password_error=password_error,
                           verpassword_error=verpassword_error,
                           title='Error')
    if not isblank(username)and not isblank(password) and not isblank(verpassword):
        return render_template('welcome.html',username=username, title='Welcome')

app.run()
