from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#DRY helper functions
def is_blank(field):
    if field == '':
        return True
    else:
        return False
def len_test(field, min, max):
    if len(field) < min or len(field) > max:
        return True
    else:
        return False
def contains_space(field):
    if " " in field:
        return True
    else:
        return False
    
@app.route('/')
def index():
    return render_template('user_signup_form.html', title="Signup Form")  

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
    
    #create blank classes for inputs that have validation errors
    uclass = ''
    pclass = ''
    vpclass = ''
    eclass = ''
    
    #username validations
    if is_blank(username):
        username_error = 'Username must not be blank'
    elif contains_space(username):
        username_error = 'Username must not contain any spaces'
    elif len_test(username, 3, 20):
        username_error = 'Username must be 3 - 20 characters in length'
        
    if username_error != '':
        uclass = 'fieldError'

        
    #Password validations
    if is_blank(password):
        password_error = 'Password must not be blank'
    elif contains_space(password):
        password_error = 'Password must not contain any spaces'
    elif len_test(password, 3, 20):
        password_error = 'Password must be 3 - 20 characters in length'
        
    if password_error != '':
        pclass = 'fieldError'
        
    #Verify Password Validation
    """if is_blank(verpassword):
        verpassword_error = 'Verify Password field must not be blank'"""
    if password != verpassword:
        verpassword_error = 'Verify Password must match Password'
        password = ''
        verpassword = ''
        
    if verpassword_error != '':
        vpclass = 'fieldError'
        
    #Email Validation
    if not is_blank(email):#if email field is not blank
        #Do these validation statements
        if len_test(email, 3, 20):
            email_error = 'Email must be 3 - 20 characters in length'
        elif " " in email:
            email_error = 'Email must not contain any spaces'
        elif "." not in email or "@" not in email:
            email_error = 'Email must be in format "something"@"something".com'
            
    if email_error != '':
        eclass = 'fieldError'
        
    if username_error or password_error or verpassword_error or email_error: #if errors
        #render user_signup_form with error messages
        return render_template('user_signup_form.html',username=username,
                           password=password,
                           verpassword=verpassword,
                           email=email,
                           username_error=username_error, 
                           uclass=uclass,
                           password_error=password_error,
                           pclass=pclass,
                           verpassword_error=verpassword_error,
                           vpclass=vpclass,
                           email_error=email_error,
                           eclass=eclass,
                           title='Error')
    else:
        #render welcome.html
        return render_template('welcome.html',username=username, title='Welcome')

app.run()
