from django.views.generic import TemplateView, ListView

from db.models import Chore


class Index(TemplateView):
    template_name = 'index.html'


class ChoreList(ListView):
    model = Chore
    template_name = 'chores/list.html'
