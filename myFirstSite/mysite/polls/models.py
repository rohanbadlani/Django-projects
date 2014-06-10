from django.db import models
from django.utils import timezone

# Create your models here.

class Poll(models.Model):
	question = models.CharField(max_length = 200)
	pub_date = models.DateTimeField()
	#was_recently_published = models.BooleanField
	"""
	def __init__(self):
		self.was_recently_published = self.was_published_recently()	
	"""
	def __unicode__(self):
		return self.question
	
	def was_published_recently(self):
		return bool(timezone.now().month - self.pub_date.month < 1)


class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	#choice_text = models.CharField(max_length = 200)	
	votes = models.IntegerField(default = 0)
	choice_text = models.CharField(max_length = 200)

	def __unicode__(self):
		return self.choice_text	
