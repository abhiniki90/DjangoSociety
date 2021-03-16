from django.contrib import admin
from .models import UserProfile
from .models import Group
from .models import Event
from .models import Feed

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Group)
admin.site.register(Event)
admin.site.register(Feed)