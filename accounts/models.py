from django.db import models
from django.contrib.auth.models import User
#2nd way to import the user from django.conf import settings
#user = OneToOneField(settings.AUTH_USER_MODEL)

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User)
	img = models.ImageField(upload_to="imagenes", blank=True, null=True)
	#followers = models.ManyToManyField(User, related_name='followers')

class Contact(models.Model):

	user_from = models.ForeignKey(User, related_name='rel_from_set')
	user_to = models.ForeignKey(User, related_name='rel_to_set')
	created = models.DateTimeField(auto_now_add=True, db_index=True)
	
	class Meta:
		ordering = ('-created',)

	def __str__(self):
		return '{} follows {}'.format(self.user_from, self.user_to)
#método del modelo usuario para agregar atributos
User.add_to_class('following', 
	models.ManyToManyField('self', 
		through=Contact, 
		related_name='followers', 
		symmetrical=False))
