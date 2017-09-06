from flask import Flask, render_template, flash, request, redirect
import cgi
import os

app = Flask (__name__)
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('signup.html')


@app.route('/', methods = ["POST"])
def signup_page():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']   

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if ' ' in username or (len(username)) < 3 or (len(username)) > 20:
        username_error = 'Not a valid username'
        username = ''

    if ' ' in password or (len(password)) < 3 or (len(password)) > 20:
        password_error = 'Not a valid password'
        password = ''

    if verify != password:
        verify_error = 'Passwords do not match'
        verify = ''

    if email != '':
        if '@' not in email or '.' not in email:
            email_error = 'Not a valid e-mail'
            email = ''
    
    if not username_error and not password_error and not verify_error and not email_error:
        signedup = username
        return redirect('/signedup?username={0}'.format(username))


    else:
        return render_template('signup.html', username_error=username_error, password_error=password_error,
        verify_error=verify_error, email_error=email_error, username=username, 
        password=password, verify=verify, email=email)


@app.route('/signedup')
def signed_up(): 
    username = request.args.get('username')
    return render_template('signedup.html', username=username )


app.run()