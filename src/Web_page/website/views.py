from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import subprocess
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/carstart', methods=['POST'])
@login_required
def carstart():
    # Run the engine_sim.py script
    try:
        result = subprocess.run(["python", "engine_sim.py"], check=True, capture_output=True, text=True)
        print(result.stdout)
        flash('Engine started successfully!', category='success')
    except subprocess.CalledProcessError as e:
        print(e.stderr)
        flash(f'Error starting engine: {e}', category='error')
    return redirect(url_for('views.car_menu'))

@views.route('/car_menu')
@login_required
def car_menu():
    return render_template("car_menu.html", user=current_user)


@views.route('/lock_unlock_door', methods=['POST'])
@login_required
def lock_unlock_door():
    action = request.form.get('action')
    script = "path_to_your_script/door.py"
    if action == "lock":
        try:
            result = subprocess.run(["python", script, "lock"], check=True, capture_output=True, text=True)
            print(result.stdout)
            flash('Door locked successfully!', category='success')
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            flash(f'Error locking door: {e}', category='error')
    elif action == "unlock":
        try:
            result = subprocess.run(["python", script, "unlock"], check=True, capture_output=True, text=True)
            print(result.stdout)
            flash('Door unlocked successfully!', category='success')
        except subprocess.CalledProcessError as e:
            print(e.stderr)
            flash(f'Error unlocking door: {e}', category='error')
    return redirect(url_for('views.car_menu'))
