# flake8: noqa

from django.urls import path, include

from . import views


urlpatterns = [
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
    path('auth/', include('django.contrib.auth.urls')),
    path('chores/', views.ChoresList.as_view(), name='chores-list'),
    path('chores/new-weekly/', views.ChoresCreateWeekly.as_view(), name='chores-create-weekly'),
    path('chores/delete-weekly/<uuid:pk>', views.ChoresDeleteWeekly.as_view(), name='chores-delete-weekly'),
    path('chores/edit-weekly/<uuid:pk>', views.ChoresUpdateWeekly.as_view(), name='chores-edit-weekly'),
    path('', views.Home.as_view(), name='home')
]
