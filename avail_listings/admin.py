from django.contrib import admin
from .models import User, Listing, Apply, Category, Event

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Apply)
admin.site.register(Category)
admin.site.register(Event)

# Created superuser account:
# username: superuser
# password: superuser
# email: superuser@email.com 
