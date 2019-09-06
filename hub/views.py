from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, CreateView, DeleteView,
    UpdateView
)

from db import models


class Home(TemplateView):
    template_name = 'home.html'


class ChoresList(TemplateView):
    template_name = 'chores/home.html'

    def get_context_data(self, *args, **kwargs):
        return {
            'chores': models.WeeklyChore.objects.all()
        }


class ChoresCreateWeekly(CreateView):
    model = models.WeeklyChore
    fields = ['name', 'assignee', 'day_of_the_week']
    template_name = 'chores/form.html'
    success_url = reverse_lazy('chores-list')


class ChoresDeleteWeekly(DeleteView):
    model = models.WeeklyChore
    template_name = 'chores/delete.html'
    success_url = reverse_lazy('chores-list')


class ChoresUpdateWeekly(UpdateView):
    model = models.WeeklyChore
    fields = ['name', 'assignee', 'day_of_the_week']
    template_name = 'chores/form.html'
    success_url = reverse_lazy('chores-list')
