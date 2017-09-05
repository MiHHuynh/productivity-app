from project import db

class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.Text)
	password = db.Column(db.Text)
	lists = db.relationship('List', backref='user', lazy='dynamic')
	blacklisted_sites = db.relationship('BlacklistedSite', secondary=blacklisted_site_user_join_table, backref=db.backref('users'))

class List(db.Model):
	__tablename__ = 'lists'

	id = db.Column(db.Integer, primary_key=True)
	name = db.column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	todo_items = db.relationship('ToDoItem', backref='list', lazy='dynamic')

class ToDoItem(db.Model):
	__tablename__ = 'todo_items'

	id = db.Column(db.Integer, primary_key=True)
	description = db.Column(db.Text)
	due_date = db.Column(db.DateTime)
	is_complete = db.Column(db.Boolean)
	is_overdue = db.Column(db.Boolean)
	list_id = db.Column(db.Integer, db.ForeignKey('lists.id'))

blacklisted_site_user_join_table = db.Table('blacklisted_site_users',
		db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
		db.Column('blacklisted_site_id', db.Integer, db.ForeignKey('blacklisted_sites.id'))
	)

class BlacklistedSite(db.Model):
	__tablename__ = 'blacklisted_sites'

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.Text)




