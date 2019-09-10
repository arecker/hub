from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy

from db.models import Chore


class Index(TemplateView):
    template_name = 'index.html'


class ChoreList(ListView):
    model = Chore
    template_name = 'chores/list.html'


class ChoreCreate(CreateView):
    model = Chore
    template_name = 'chores/form.html'
    fields = ['name', 'assignee', 'cadence', 'next_due_date']
    success_url = reverse_lazy('chore-list')
