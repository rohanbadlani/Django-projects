from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from poll_votes.models import Poll2, Choice2

class IndexView(generic.ListView):
        print "\n Inside IndexView \n"
        template_name = 'poll_votes/index.html'
        context_object_name = 'latest_poll_list'
        print "\ncontext_obj list:", context_object_name

        def get_queryset(self):	
                """Return the lst five published Polls"""
                print "\n inside get query\n"
        	return Poll2.objects.order_by('-pub_date')[:5]
        
class DetailView(generic.DetailView):
	model = Poll2
	#print "\n Poll2::question \n", Poll2.objects.all()
	#print "\n inside details view\n"
        #context_object_name = 'latest_poll_list'
	template_name = 'poll_votes/detail.html'
	

class ResultView(generic.DetailView):
	model = Poll2
	template_name = 'poll_votes/result.html'


def votes(request, poll_id):
	return HttpResponse("This is the results page")
	"""poll = get_object_or_404(Poll2, pk = poll_id)
	try:
		selected_choice = poll.choice_set.get(pk = request.POST['choice']
	except (KeyError, Choice2.DoesNotExist):
		return render(request, 'poll_votes/details.html',
			{'poll':poll,
			 'error_message':"You have not selected any choice. Kindly select one and then use it."
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		
		return HttpResponseRedirect(reverse('poll_votes/results.html', args = (poll.id,)))
		
"""

# Create your views here.

