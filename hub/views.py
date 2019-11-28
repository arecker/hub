from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, ListView, CreateView,
    UpdateView, DeleteView, View
)

from db.models import Chore, Contact, Campaign
from hub.forms import ChoreForm


class Index(TemplateView):
    template_name = 'index.html'


class ChoreList(ListView):
    model = Chore
    template_name = 'chores/list.html'

    def get_queryset(self):
        qs = super(ChoreList, self).get_queryset()

        date_filter = self.request.GET.get('date_filter', 'today')

        if date_filter == 'today':
            qs = qs.due_today()
        elif date_filter == 'three-days':
            qs = qs.due_next_three_days()

        return qs.order_by('next_due_date')

    def get_context_data(self, **kwargs):
        context = super(ChoreList, self).get_context_data(**kwargs)
        context['date_filter'] = self.request.GET.get('date_filter', 'today')
        context['active'] = 'chores'
        return context


class ChoreCreate(CreateView):
    model = Chore
    template_name = 'generic/form.html'
    form_class = ChoreForm

    def get_success_url(self, **kwargs):
        url = reverse_lazy('chore-list') + f'?{self.request.GET.urlencode()}'
        return url

    def get_context_data(self, **kwargs):
        context = super(ChoreCreate, self).get_context_data(**kwargs)
        context['active'] = 'chores'
        return context


class ChoreUpdate(UpdateView):
    model = Chore
    template_name = 'chores/generic.html'
    form_class = ChoreForm

    def get_success_url(self, **kwargs):
        url = reverse_lazy('chore-list') + f'?{self.request.GET.urlencode()}'
        return url

    def get_context_data(self, **kwargs):
        context = super(ChoreUpdate, self).get_context_data(**kwargs)
        context['active'] = 'chores'
        return context


class ChoreDelete(DeleteView):
    model = Chore
    template_name = 'generic/delete.html'

    def get_success_url(self, **kwargs):
        url = reverse_lazy('chore-list') + f'?{self.request.GET.urlencode()}'
        return url

    def get_context_data(self, **kwargs):
        context = super(ChoreDelete, self).get_context_data(**kwargs)
        context['active'] = 'chores'
        return context


class ChoreComplete(View):
    def get(self, request, pk):
        chore = get_object_or_404(Chore, pk=pk)
        chore.next_due_date = chore.find_next_due_date()
        chore.save()
        url = reverse_lazy('chore-list') + f'?{request.GET.urlencode()}'
        return redirect(url)


class CampaignList(ListView):
    model = Campaign
    template_name = 'campaigns/list.html'

    def get_context_data(self, **kwargs):
        context = super(CampaignList, self).get_context_data(**kwargs)
        context['active'] = 'contacts'
        return context


class CampaignCreate(CreateView):
    model = Campaign
    fields = ['name']
    template_name = 'generic/form.html'
    success_url = reverse_lazy('campaign-list')

    def get_context_data(self, **kwargs):
        context = super(CampaignCreate, self).get_context_data(**kwargs)
        context['active'] = 'contacts'
        return context


class CampaignUpdate(UpdateView):
    model = Campaign
    fields = ['name']
    template_name = 'generic/form.html'

    def get_context_data(self, **kwargs):
        context = super(CampaignUpdate, self).get_context_data(**kwargs)
        context['active'] = 'contacts'
        return context


class CampaignDelete(DeleteView):
    model = Campaign
    template_name = 'generic/delete.html'
    success_url = reverse_lazy('campaign-list')

    def get_context_data(self, **kwargs):
        context = super(CampaignDelete, self).get_context_data(**kwargs)
        context['active'] = 'contacts'
        return context
