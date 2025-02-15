from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Lab
from .models import Member
from .models import Opportunity

admin.site.register(Lab)
admin.site.register(Member)
admin.site.register(Opportunity)