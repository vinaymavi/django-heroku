from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Question
from .models import Choice
import logging

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    print "Index page loading.."
    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    template_name = "polls/detail.html"
    model = Question


class ResultView(generic.DetailView):
    content_type = ContentType.objects.get_for_model(Question)
    # permission = Permission.objects.create(codename="show_result", name="Show results", content_type=content_type)
    template_name = "polls/results.html"
    model = Question


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    content_type = ContentType.objects.get_for_model(Question)
    # permission = Permission.objects.create(codename="vote_poll", name="Vote Polls", content_type=content_type)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        render(request, 'polls/detail.html', {"question": question, "error_msg": "Choice not defined."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
