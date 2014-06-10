from django.shortcuts import render
from django.http import HttpResponse
from mongokit import Connection
from computers.models import Computer

def index(request):
	return render(request, 'computers/index.html')

def details(request):
	if request.method == 'POST':
		if request.POST.get("computer_details"):
			print "You have successfully submitted the foem"
			conn = Connection()
			conn.register([Computer])
			database = conn.mydb
			collection = database.mycollection
			computer = collection.Computer()
			computer.make = unicode(request.POST['make'])
			computer.model = unicode(request.POST['model'])
			computer.purchase_date = unicode(request.POST['pur_date'])
			computer.cpu_ghz = unicode(request.POST['cpu_speed'])
			computer.save()
			print "Computer is:::" + str(computer.model)
			computer_list = collection.Computer.find()
			context = {'computer_list': computer_list}
			return render(request, 'computers/details.html', context)
			#return HttpResponse("Your response has been recorded")
		else:
			print "You havent clicked submit as yet"

	return HttpResponse("You response was not successfully recd")
			
	
		
# Create your views here.
