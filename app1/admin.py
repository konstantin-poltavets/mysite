from django.contrib import admin
from .models import zbdoor, zbbtn, zbtmphum


#admin.site.register(zbdoor)
#admin.site.register(zbbtn)
#admin.site.register(zbtmphum)


# Define the admin class
class ZbtmphumAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_date', 'temperature', 'humidity')

# Register the admin class with the associated model
admin.site.register(zbtmphum, ZbtmphumAdmin)

@admin.register(zbbtn)
class ZbbtnAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_date', 'action', 'voltage')

@admin.register(zbdoor)
class ZbdoorAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_date', 'contact', 'voltage')
    list_filter = ('topic', 'created_date', 'contact')

