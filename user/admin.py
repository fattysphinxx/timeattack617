from django.contrib import admin
from user.models import User, UserProfile,UserType

# Register your models here.


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(UserType)


