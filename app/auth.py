
import functools
from . import gencaptcha
from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)

bp = Blueprint('auth', __name__, url_prefix='/auth')


@ bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        error = None
        password = request.form['password']
        user = {'username': 'user1', 'password': password, 'id': 1}

        if user is None:
            error = 'Incorrect username.'
        if not password == session['captcha']:
            error = 'Incorrect password.'
        if error is None:
            session.clear()
            session['user_id'] = 'Login_Succes'
            return redirect(url_for('index'))
        flash(error)
    # Generate a new CAPTCHA text
    captcha_text = gencaptcha.generate_random_string()
    session['captcha'] = captcha_text
    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))
