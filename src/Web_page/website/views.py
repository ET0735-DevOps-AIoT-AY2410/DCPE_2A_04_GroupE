from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
import json
import subprocess
from flask import Flask, render_template
import threading
import time
from website import temp
from website import fuel
from website import Door
from website import rfid_checker
from website import ultrasound
from website import engine_sim
from website import aircon
import subprocess
from website import buzzer
from website import switch 

    
views = Blueprint('views', __name__)


door_status = "closed"
theft_detected = False

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
    
@views.route('/get_door_status', methods=['GET'])
@login_required
def get_door_status():
    global door_status, theft_detected
    return jsonify({"doorStatus": door_status, "theft_status": "Detected" if theft_detected else "Not Triggered"})

@views.route('/lock_unlock_door', methods=['POST'])
def lock_unlock_door():
    global door_status
    data = request.get_json()
    action = data.get('action')
    if action == 'lock':
        Door.lock_door()
        door_status = 'locked'
        print("locked")
    else:
        Door.unlock_door()
        door_status = 'unlocked'
        print("unlocked")
    return jsonify({"success": True})


def check_theft():
    global theft_detected, door_status
    while True:
        if door_status == "locked" and switch.switch_Status() == 1:  # Assuming switch is active low
            theft_detected = buzzer.buzzer_on()
        if door_status == "locked" and ultrasound.get_distance()<10:
            theft_detected = buzzer.buzzer_on()  
        else:
            theft_detected = False
        time.sleep(0.1)  




def start_threads():
    threading.Thread(target=check_theft, daemon=True).start()