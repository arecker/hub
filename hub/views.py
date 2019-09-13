from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, CreateView,
    UpdateView, DeleteView, View
)

from db.models import Chore
from hub.forms import ChoreForm


class Index(TemplateView):
    template_name = 'index.html'


class ChoreList(ListView):
    model = Chore
    template_name = 'chores/list.html'

    def get_queryset(self):
        qs = super(ChoreList, self).get_queryset()

        date_filter = self.request.GET.get('date_filter', 'today')
        assignee_filter = self.request.GET.get('assignee_filter', 'mine')

        if date_filter == 'today':
            qs = qs.due_today()
        elif date_filter == 'three-days':
            qs = qs.due_next_three_days()

        if assignee_filter == 'mine':
            qs = qs.filter(assignee=self.request.user)

        return qs.order_by('next_due_date')

    def get_context_data(self, **kwargs):
        context = super(ChoreList, self).get_context_data(**kwargs)
        context['date_filter'] = self.request.GET.get('date_filter', 'today')
        context['assignee_filter'] = self.request.GET.get('assignee_filter', 'mine')
        return context


class ChoreCreate(CreateView):
    model = Chore
    template_name = 'chores/form.html'
    form_class = ChoreForm
    success_url = reverse_lazy('chore-list')


class ChoreUpdate(UpdateView):
    model = Chore
    template_name = 'chores/form.html'
    form_class = ChoreForm
    success_url = reverse_lazy('chore-list')


class ChoreDelete(DeleteView):
    model = Chore
    template_name = 'chores/delete.html'
    success_url = reverse_lazy('chore-list')


class ChoreComplete(View):
    def get(self, request, pk):
        context = {'chore': get_object_or_404(Chore, pk=pk)}
        return render(request, 'chores/complete.html', context)

    def post(self, request, pk):
        chore = get_object_or_404(Chore, pk=pk)
        chore.next_due_date = chore.find_next_due_date()
        chore.save()
        return redirect('chore-list')
