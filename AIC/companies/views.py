from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from companies.models import Company, Discipline

def index(request):
	company_list = Company.objects.all()
	context = {'company_list': company_list}
	return render(request, 'companies/index.html', context)

def discipline(request):
	discipline_list = Discipline.objects.all()
	context = {'discipline_list': discipline_list}
	return render(request, 'companies/discipline.html', context)


def specific(request, discipline_id):

	company_list = Company.objects.filter(discipline = discipline_id)
	#print 'Companies' + str(company_list)
	context = {'company_list': company_list}
	return render(request, 'companies/specific.html', context)		

def details(request, company_id):
	company = get_object_or_404(Company, pk = company_id)
	context = {'company': company, 'companyname': company.name, 'companycontact_name': company.contact_name, 'companycontact_phone': company.contact_phone, 'companydiscipline': company.discipline}
	
	return render(request, 'companies/details.html', context)
	
	
	

# Create your views here.
