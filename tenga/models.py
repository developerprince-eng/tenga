import datetime
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import backref
from sqlalchemy.dialects.postgresql import JSON
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, lm

class User(db.Model, UserMixin):
	__tablename__ = 'users'
	""" User model defines the user tabel in the database """
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(120), unique=True, index=True, nullable=False)
	first_name = db.Column(db.String(120))
	surname = db.Column(db.String(120))
	email = db.Column(db.String(120), unique=True,index=True)
	salt = db.Column(db.String(72))
	password_hash = db.Column(db.String(200))
	dob = db.Column(db.Date)
	

	def save(self):
		db.session.add(self)
		db.session.commit()
	

	@staticmethod
	@lm.user_loader
	def load_user(user_id):
		return User.query.get(user_id)
	

	def is_authenticate(self):
		return True
	

	def is_active(self):
		return True
	

	def is_anonymous(self):
		return False
	

	def get_id(self):
		return False
	

	def __repr__(self):
		return '<User %r>' % self.username
	

	@property
	def password(self):
		raise AttributeError('password: write-only field')
	

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)
	

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)
	

	@staticmethod
	def get_by_email(email):
		return User.query.filter_by(email=email).first()
	

