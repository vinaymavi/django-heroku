# Capture single of  django.contrib.auth.Group class.

from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
import logging
from  polls.models import Question

logger = logging.getLogger(__name__)


def create_group_permission(sender, **kwargs):
    print "Single calling."
    print kwargs
    print kwargs['instance'].name
    name = kwargs['instance'].name
    if kwargs['created']:
        content_type = ContentType.objects.get_for_model(Question)
        permission = Permission.objects.create(codename=name, name=name + " member", content_type=content_type)


post_save.connect(create_group_permission, sender=Group)
