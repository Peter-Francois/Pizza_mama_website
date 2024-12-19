from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ingredients','vegetarienne', 'prix')
# Register your models here.


admin.site.register(Pizza, PizzaAdmin)
