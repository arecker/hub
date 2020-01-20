# flake8: noqa

from django.urls import path, include

from hub import views, api

urlpatterns = [
    path('chores/', views.ChoreList.as_view(), name='chore-list'),
    path('chores/create', views.ChoreCreate.as_view(), name='chore-create'),
    path('chores/complete/<uuid:pk>/', views.ChoreComplete.as_view(), name='chore-complete'),
    path('chores/update/<uuid:pk>/', views.ChoreUpdate.as_view(), name='chore-update'),
    path('chores/delete/<uuid:pk>/', views.ChoreDelete.as_view(), name='chore-delete'),
    path('api/', include(api.router.urls)),
    path('', views.Index.as_view(), name='index')
]
