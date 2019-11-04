from django.contrib import admin

# Register your models here.
from models import Poll

admin.site.register(Poll)
from django.contrib.auth.models import User

users = User.objects.all()
print(users)