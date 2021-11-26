from django.contrib import admin

from boletim.models import BimestreModel, BoletimModel

# Register your models here.
admin.site.register(BimestreModel)
admin.site.register(BoletimModel)