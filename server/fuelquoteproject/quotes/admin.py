from django.contrib import admin
from .models import FuelQuote, FuelQuoteModifier

# Register your models here.

class FuelQuoteAdmin(admin.ModelAdmin):
  list_display = ('id','user','delivery_date' ,'delivery_state', 'total_amount_due')
  list_display_links = ('user', 'delivery_date', 'total_amount_due')

class FuelQuoteModAdmin(admin.ModelAdmin):
  list_display = ('id','price_per_gallon', 'summer_modifier', 'profit_margin')
  list_display_links = ('id', 'price_per_gallon' )
admin.site.register(FuelQuote, FuelQuoteAdmin)
admin.site.register(FuelQuoteModifier, FuelQuoteModAdmin)



