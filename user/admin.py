from django.contrib import admin
from user.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)