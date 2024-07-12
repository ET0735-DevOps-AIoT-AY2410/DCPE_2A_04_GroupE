from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
import subprocess
from flask import Flask, render_template
import threading
import time
from website import temp
from website import fuel
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
    script = "Door.py"
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


@views.route('/get_temperature')
@login_required
def get_temperature():
    temperature = temp.read_temp_humidity()
    return jsonify({'temperature': temperature})
    
@views.route('/get_FuelLevel')
@login_required
def get_FuelLevel():
    FuelLevel = fuel.get_fuel_level(0)
    return jsonify({'fuel': FuelLevel})

@views.route('/set_aircon_temperature', methods=['POST'])
@login_required
def set_aircon_temperature():
    try:
        data = request.get_json()
        temperature = data['temperature']
        
        # Call the aircon.py script with the temperature argument
        result = subprocess.run(['python3', 'aircon.py', str(temperature)], capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False, 'error': result.stderr}), 500
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500
