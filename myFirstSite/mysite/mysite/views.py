from django.http import HttpResponse
	
def home(request):
	return HttpResponse("<H1>This is the home page</H1>")

