from django.db import models
from django.conf import settings

# Create your models here.
# The user 'one-to-one' field allows us to associate profiles with
# users. We use CASCADE for the 'on_delete' parameter so that its related
# profile also gets deleted when a user is deleted. The photo field is an
# ImageField field. We will need to install the Pillow library to handle
# images.
class user_profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to = 'user/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)



