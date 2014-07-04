from django.utils.translation import ugettext as _
from django.db import models
from django.contrib.auth.models import User
 
 
class UserProfile(models.Model):
    """
    A model to store extra information for each user.
    """
    user = models.OneToOneField(User, related_name='profile')
    gender = models.CharField(_("gender"), max_length=10)
    birth_year = models.PositiveIntegerField(_("birth year"))
 
    def __unicode__(self):
        return self.user.get_full_name()
 

from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=get_user_model())
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print 'horreeeyyyyyyyyyyyyyyyyyyy'
    if created:
        Token.objects.create(user=instance)


 