from flask import Flask
import os

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

# Create blueprint
bp = Blueprint('modeling', __name__, url_prefix='/modeling')

# Define general modeling 
@bp.route('/', methods=('GET', 'POST'))
def modeling():
    if request.method == "POST":
        flash(request.form)
        flash("update model and stuff")
    return render_template('base.html')

@bp.route('/predict', methods=['POST'])
def predict():
    return render_template('base.html', prediction=True)

@bp.route('/graph', methods=['GET'])
def graph():
    if request.method == "GET":
        flash('graph stuff here')
        print(session.get('user_id'))
    return render_template('base.html')
        
@bp.before_app_request
def load():
    user_id = session.get('user_id')
    if user_id is None:
        print("none")