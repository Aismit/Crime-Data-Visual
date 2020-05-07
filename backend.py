from flask import Flask, jsonify, request, Response, render_template, url_for
from flask_api import status
from MySQLdb import _mysql
import mysql.connector
import numpy as np
import os, json, requests



app = Flask(__name__)

query_parts = {}

# with app.app_context(), app.test_request_context():
# 	print(url_for('static', filename='css/selection.css', _external =True), flush=True)

@app.route('/', methods=["GET"])
def get_selection_page():
	#with app.app_context(), app.test_request_context():
		#print(url_for('static', filename='css/selection.css', _external =True), flush=True)
	return render_template('selection.html')

# @app.route('/police', methods=["POST"]):
# def get_police_page():
# 	path = request.form()
# 	return 
@app.route('/visualize', methods=["POST"])
def visualize():
	print("hjsdfsdfs", flush=True)
	#val = request.form['value']
	print(request.form, flush=True)
	print(request.form['value1'], flush=True)
	return render_template('visualize.html')

@app.route('/crimes', methods=["GET", "POST"])
def crimes():
	global query_parts
	query_parts['info'] = 'crimes'
	print("YESS", flush=True)
	return render_template('crimez.html')

@app.route('/offenders', methods=["GET"])
def offenders():
	global query_parts
	query_parts['info'] = 'offenders'
	return render_template('offenders.html')


@app.route('/nyc', methods=["GET"])
def nyc():
	global query_parts
	query_parts['location'] = 'nyc'
	return render_template('nyc.html')


@app.route('/atl', methods=["GET"])
def atl():
	global query_parts
	query_parts['location'] = 'atl'
	return render_template('atl.html')

@app.route('/aus', methods=["GET"])
def aus():
	global query_parts
	query_parts['location'] = 'aus'
	return render_template('aus.html')

@app.route('/chi', methods=["GET"])
def chi():
	global query_parts
	query_parts['chi'] = 'chi'
	return render_template('chi.html')

@app.route('/journalist', methods=["GET"])
def journalist():
	return render_template('journalist.html')

if __name__ == '__main__':
    db = mysql.connector.connect(host='db290tproj', user='root', passwd='pw', database='db290TProj')
    cursor = db.cursor(buffered=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)