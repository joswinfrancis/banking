from django.contrib import admin

# Register your models here.
from .models import District, Branch

admin.site.register(District)
admin.site.register(Branch)