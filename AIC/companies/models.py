from django.db import models



class Discipline(models.Model):
	name = models.CharField(max_length = 100)
	text = models.CharField(max_length = 100)
		
	def __unicode__(self):
		return self.name


class Company(models.Model):
	discipline = models.ForeignKey(Discipline)
	name = models.CharField(max_length = 100)
	contact_name = models.CharField(max_length = 100)
	contact_phone = models.IntegerField(max_length = 10)
	logo = models.ImageField(upload_to = ('company_logo'), max_length = 50, blank = True)

	def __unicode__(self):
		return self.name

# Create your models here.
