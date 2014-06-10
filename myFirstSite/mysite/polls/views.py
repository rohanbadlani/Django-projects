from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from polls.models import Poll, Choice
from django.template import RequestContext, loader
from django.http import Http404
from django.core.urlresolvers import reverse

"""
def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {'latest_poll_list':latest_poll_list})
	return HttpResponse(template.render(context))
"""

def index(request):
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_poll_list': latest_poll_list}
	return render(request, 'polls/index.html', context)
"""	
def results(request, poll_id):
	return HttpResponse("This is the result for the poll number: %s" %poll_id)
"""
"""
def detail(request, poll_id):
	try:
		poll = Poll.objects.get(pk = poll_id)
	except:
		raise Http404
	return render(request, 'polls/detail.html', {'poll':poll})
"""

def detail(request, poll_id):
	poll = get_object_or_404(Poll, pk = poll_id)
	context = {'poll':poll}
	return render(request, 'polls/detail.html', context)	

def votes(request, poll_id):
	poll = get_object_or_404(Poll, pk = poll_id)
	try: 
 		selected_choice = poll.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		context = {'poll':poll, 'error_message':"You did not select any choice. kindly select one"}
	
		return render(request, 'polls/detail.html', context)
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:poll_results', args = (poll.id,)))

def results(request, poll_id):
	poll = get_object_or_404(Poll, pk = poll_id)
	return render(request, 'polls/results.html', {'poll':poll})




# Create your views here.
