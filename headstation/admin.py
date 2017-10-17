from django.contrib import admin

from .models import User, TemperatureReading, HumidityReading, co2Reading, ErrorLog

# include databases on admin site for editing
admin.site.register(User)
admin.site.register(TemperatureReading)
admin.site.register(HumidityReading)
admin.site.register(co2Reading)
admin.site.register(ErrorLog)