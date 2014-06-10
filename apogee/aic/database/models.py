
from django.db import models

class Discipline(models.Model):
	stream_name = models.CharField('Stream Name*', max_length = 50)
	stream_code = models.CharField('Stream Code*', max_length = 2)
	
	def __unicode__(self):
		return self.stream_name
	

class Company(models.Model):
	company_name = models.CharField('Company Name*', max_length = 100)
	contact_name = models.CharField('Contact Name*', max_length = 100)
	contact_phone = models.CharField('Contact Phone', max_length = 13, default = '+91', blank = True)
	contact_email = models.EmailField('Contact Email*', max_length = 100)
	discipline = models.ForeignKey(Discipline)
	allowed_onsite = models.BooleanField('Display On Site?', default = True)
	
	def __unicode__(self):
		return self.company_name


class Problem(models.Model):
	problem_title = models.CharField('Problem Title*', max_length = 200)
	discipline = models.ForeignKey(Discipline)
	company = models.ForeignKey(Company)
	problem_text = models.CharField('Enter Some Details About The Problem', max_length = 500, blank = True)
	publish_date = models.DateTimeField(null = True)
	submit_by = models.DateTimeField()
	allowed_onsite = models.BooleanField('Display On Site?', default = True)
	
	def __unicode__(self):
		return self.problem_title


# Create your models here.
