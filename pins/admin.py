from django.contrib import admin
from .models import Pin, Pinner, Board, Image


admin.site.register(Pin)
admin.site.register(Pinner)
admin.site.register(Image)
admin.site.register(Board)
