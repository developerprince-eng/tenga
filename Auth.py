import bcrypt

def get_hash_for_user(user):
	return user.password

def get_salt_for_user(user):
	return user.salt

def create_password_hash(password):
	salt = bcrypt.gensalt(16)
	hashed_pass = bcrypt.hashpw(password, salt)
	return hashed_pass, salt

def check_hash_for_user(password, user):
	stored_hash = get_hash_for_user(user)
	generated_hash = recreate_hash(password, get_hash_for_user(user))
	return hashed_pass, salt

def recreate_hash(password, salt):
	hash_pass = bcrypt.hashpw(str(password), str(salt))
	return hash_pass

def validate(user, password):
	if(check_hash_for_user(password, user)):
		return True
	 else:
		return False