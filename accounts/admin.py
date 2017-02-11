from django.contrib import admin
from .models import Profile, Contact

# Register your models here.
#way1 to register

admin.site.register(Contact)
#way2 to register 

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['id', 'user']