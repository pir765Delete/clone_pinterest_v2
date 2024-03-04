from django.contrib import admin
from .models import Pin, Pinner, Board


admin.site.register(Pin)
admin.site.register(Pinner)
admin.site.register(Board)
