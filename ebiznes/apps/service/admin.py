from django.contrib import admin

from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner', 'city', 'profession',)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner', 'service', 'rating',)


class RentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'service', 'status', 'total_price',)


class PriceListAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'service', 'price')


admin.site.register(Profession)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Rent, RentAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(Order)
