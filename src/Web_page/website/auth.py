from flask import Blueprint, render_template, request, flash, redirect, url_for , session
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db   ##means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user
import random
import string
import smtplib
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

auth = Blueprint('auth', __name__)


def generate_2fa_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_2fa_code(email, code):
    # Email configuration
    smtp_server = 'smtp.gmail.com'  # For Gmail
    smtp_port = 587
    smtp_username = 'ezelllowgaming@gmail.com'
    smtp_password = 'T0611022z'  # Consider using environment variables for sensitive data

    # Create the email
    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = email
    msg['Subject'] = 'Your 2FA Code'

    body = f'Your 2FA code is: {code}'
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        text = msg.as_string()
        server.sendmail(smtp_username, email, text)
        server.quit()
        print(f"2FA code sent to {email}")
    except Exception as e:
        print(f"Failed to send 2FA code: {e}")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
#                flash('Logged in successfully!', category='success')
#                login_user(user, remember=True)
#                return redirect(url_for('views.home'))
                code = generate_2fa_code()
                user.two_factor_code = code
                db.session.commit()
                send_2fa_code(user.email, code)
                session['email'] = email
                return redirect(url_for('auth.verify_2fa'))    
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/verify_2fa', methods=['GET', 'POST'])
def verify_2fa():
    if request.method == 'POST':
        code = request.form.get('code')
        email = session.get('email')
        user = User.query.filter_by(email=email).first()
        if user and user.two_factor_code == code:
            login_user(user)
            return redirect(url_for('views.home'))
        else:
            flash('Invalid 2FA code.', 'danger')
    return render_template('verify_2fa.html')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        verification_code = request.form.get('verification_code')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        elif verification_code != '123':
            flash('Incorrect verification code.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)