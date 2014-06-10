from django.contrib import admin

from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class ChoiceAdmin(admin.ModelAdmin):
	fieldsets = [
	('Associated Poll', {'fields':['poll']}),
	('Choice Info', {'fields':['votes','choice_text']})
	]
	
class ChoiceTabular(admin.TabularInline):
	model = Choice
	extra = 3
	
	
class PollAdmin(admin.ModelAdmin):
	#fields = ['question']
	fieldsets = [
	(None, {'fields': ['question']}),
	('Date information', {'fields': ['pub_date'], 'classes': ['collapse']})
	]
	inlines = [ChoiceTabular]
	list_display = ('question', 'pub_date', 'was_published_recently')	
	search_fields = ['question']
	list_filter = ['pub_date']
	"""
	was_published_recently.boolean = True
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.short_description = 'Published Recently?'
	"""
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice, ChoiceAdmin)
# Register your models here.
