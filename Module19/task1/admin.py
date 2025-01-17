from django.contrib import admin
from task1.models import Buyer, Game


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance', 'age',)
    search_fields = ('name', 'age',)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'cost', 'size', 'description', 'age_limited',)
    list_filter =('title', 'cost','description')
    fieldsets = (
        ('main_info',{
            'fields': ('title', 'cost', 'age_limited')
        }),
        ('additional_info',{
            'fields': ('size', 'description')
        }),
    )