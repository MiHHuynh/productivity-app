from project import db

blacklisted_site_user_join_table = db.Table('blacklisted_site_users',
		db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
		db.Column('blacklisted_site_id', db.Integer, db.ForeignKey('blacklisted_sites.id'))
	)

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.Text, unique=True, nullable=False)
	password = db.Column(db.Text, nullable=False)
	lists = db.relationship('List', backref='user', lazy='dynamic')
	blacklisted_sites = db.relationship('BlacklistedSite', secondary=blacklisted_site_user_join_table, backref=db.backref('users'))

	def __init__(self, email, password):
		self.email = email
		self.password = password

	# def calc_punctuality_percentage(self):
	# 	pass

class List(db.Model):
	__tablename__ = 'lists'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	todo_items = db.relationship('ToDoItem', backref='list', lazy='dynamic')

	def __init__(self, name, user_id):
		self.name = name
		self.user_id = user_id

class ToDoItem(db.Model):
	__tablename__ = 'todo_items'

	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text, nullable=False)
	due_date = db.Column(db.DateTime)
	is_complete = db.Column(db.Boolean)
	list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))

	def __init__(self, description, due_date, list_id):
		self.description = description
		self.due_date = due_date
		self.is_complete = False
		self.list_id = list_id

	# def is_overdue(self)
	# 	pass

		#todo.is_overdue()



class BlacklistedSite(db.Model):
	__tablename__ = 'blacklisted_sites'

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.Text, unique=True, nullable=False)

	def __init__(self, url):
		self.url = url


