from django.contrib import admin
from .models import Specialist, Service, Appointment, Review, FAQ

admin.site.register(Specialist)
admin.site.register(Service)
admin.site.register(Appointment)
admin.site.register(Review)
admin.site.register(FAQ)