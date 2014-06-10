from django.contrib import admin
from database.models import Company, Discipline, Problem

admin.site.register(Discipline)
admin.site.register(Company)
admin.site.register(Problem)

# Register your models here.
