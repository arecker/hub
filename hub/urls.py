# flake8: noqa

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from hub import views, api

urlpatterns = [
    path('chores/', views.ChoreList.as_view(), name='chore-list'),
    path('chores/create', views.ChoreCreate.as_view(), name='chore-create'),
    path('chores/complete/<uuid:pk>/', views.ChoreComplete.as_view(), name='chore-complete'),
    path('chores/update/<uuid:pk>/', views.ChoreUpdate.as_view(), name='chore-update'),
    path('chores/delete/<uuid:pk>/', views.ChoreDelete.as_view(), name='chore-delete'),

    path('wallpapers/', views.WallpaperList.as_view(), name='wallpaper-list'),
    path('wallpapers/create', views.WallpaperCreate.as_view(), name='wallpaper-create'),
    path('wallpapers/<uuid:pk>/', views.WallpaperDelete.as_view(), name='wallpaper-delete'),

    path('api/', include(api.router.urls)),
    path('', views.Index.as_view(), name='index')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
