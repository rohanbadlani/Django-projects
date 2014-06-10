import datetime
	
from django.db import models
from django_mongokit import connection
from mongokit import Document

class Computer(Document):
	structure = {
		'make': unicode, 
		'model': unicode, 
		'purchase_date': unicode,
		'cpu_ghz': unicode,
	}
	
	validators = {
		'cpu_ghz': lambda x: x>0,
		'make': lambda x: x.strip(),
	}
	
	default_values = {
		'purchase_date': datetime.datetime.utcnow,
	}

	use_dot_notation = True
	
	indexes = [
		{'fields': ['make']},
	]
	
connection.register([Computer])

# Create your models here.
