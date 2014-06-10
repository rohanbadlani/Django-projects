from django.db import models

class Poll2(models.Model):
	question = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return self.question

	def was_published_recently(self):
		self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published Recently?'
	

class Choice2(models.Model):
	poll = models.ForeignKey(Poll2)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default =  0)

	def __unicode__(self):
		return "Text::" + self.choice_text + "::Votes::" + str(self.votes)



	
# Register your models here.
