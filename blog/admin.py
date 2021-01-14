from django.contrib import admin

# Register your models here.
from .models import Jobseekers
from .models import Company

admin.site.register(Jobseekers) 
admin.site.register(Company) 