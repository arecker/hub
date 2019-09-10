from django.shortcuts import get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, CreateView, DeleteView,
    UpdateView, View
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


class ChoresComplete(View):
    def get(self, request, choretype, pk):
        try:
            model = {
                'weekly': models.WeeklyChore,
                'monthly': models.MonthlyChore
            }[choretype]
            chore = get_object_or_404(model, pk=pk)
            chore.complete(now=chore.next_due)
            chore.save()
            return redirect('chores-list')
        except KeyError:
            return Http404()
