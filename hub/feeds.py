from django.contrib.syndication.views import Feed

from db import models


class WallpaperFeed(Feed):
    title = 'Wallpapers'
    description = 'Wallpapers, from the hub.'
    link = '/wallpapers/feed/'

    def items(self):
        return models.Wallpaper.objects.all()

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.name

    def item_link(self, item):
        return item.image.url
