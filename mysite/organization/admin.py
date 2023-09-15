from django.contrib import admin

from .models import Customer, Organization, Office

admin.site.register(Customer)
admin.site.register(Organization)
admin.site.register(Office)


