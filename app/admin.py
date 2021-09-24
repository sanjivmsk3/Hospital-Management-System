from django.contrib import admin
from app.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Branch)

class Patin(admin.ModelAdmin):
    list_display = ("user","id","name","mobile","age","date")

admin.site.register(Paitent,Patin)