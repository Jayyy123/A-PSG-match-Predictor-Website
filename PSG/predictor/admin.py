from django.contrib import admin

from predictor.models import PsgPredictor, Result

admin.site.register(PsgPredictor)
admin.site.register(Result)
