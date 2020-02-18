import logging
import os

from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Wallpaper


logger = logging.getLogger('hub')


@receiver(post_delete, sender=Wallpaper)
def cleanup_wallpaper_image(sender, instance, *args, **kwargs):
    target = os.path.join(settings.MEDIA_ROOT, instance.image.path)
    if os.path.exists(target):
        os.remove(target)
        logger.info('%s triggered media cleanup, deleted %s', instance, target)
    else:
        logger.info('skipping media cleanup for %s, %s does not exist', instance, target)
