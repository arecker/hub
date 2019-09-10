# flake8: noqa

from django.urls import path, include
from django.contrib.auth.decorators import login_required

from hub import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('chores/', login_required(views.ChoreList.as_view()), name='chore-list'),
    path('chores/create', login_required(views.ChoreCreate.as_view()), name='chore-create'),
    path('', login_required(views.Index.as_view()), name='index')
]
