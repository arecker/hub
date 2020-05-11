from rest_framework import serializers, viewsets, routers, decorators
from rest_framework.response import Response

from db import models


class ChoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Chore
        fields = ['id', 'name', 'assignee', 'cadence', 'next_due_date']


class ChoreViewSet(viewsets.ModelViewSet):
    queryset = models.Chore.objects.all()
    serializer_class = ChoreSerializer


class WallpaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Wallpaper
        fields = ['name', 'image']


class WallpaperViewSet(viewsets.ModelViewSet):
    queryset = models.Wallpaper.objects.all()
    serializer_class = WallpaperSerializer

    @decorators.action(detail=False)
    def random(self, request):
        choice = self.get_serializer(self.queryset.order_by('?').first())
        return Response(choice.data)


router = routers.DefaultRouter()
router.register('chores', ChoreViewSet, 'api-chore-list')
# router.register('wallpapers', WallpaperViewSet, 'api-wallpaper-list')
