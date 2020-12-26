import os
from flask import flash, redirect, render_template, url_for, request
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
from . import app

#BAD REQUEST
@app.errorhandler(400)
def resource_error(e):
	return render_template('400.html'), 400

#FORBIDDEN ERROR
@app.errorhandler(403)
def forbidden(e):
	return render_template('403.html'), 403

#NOT ALLOWED ERROR
@app.errorhandler(405)
def method_not_allowed(e):
	return render_template('405.html'), 405

#NOT FOUND ERROR
@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

#SERVER INTERNAL ERROR
@app.errorhandler(500)
def server_error(e):
	return render_template('500.html'), 500

#BAD GATEWAY
@app.errorhandler(502)
def server_error_bad_gateway(e):
	return render_template('502.html'), 502

#GATEWAY TIMEOUT
@app.errorhandler(504)
def server_error_gateway_timeout(e):
	return render_template('504.html'), 504

#HOME PAGE INDEX
@app.route("/", methods=['GET'])
def index():
	return render_template("index.html")