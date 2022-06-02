from django.contrib import admin
from .models import *
from home.models import Player

# Register your models here.
admin.site.register(Questions)
admin.site.register(Player)
admin.site.register(Questionsds)
admin.site.register(Questionsdbms)
