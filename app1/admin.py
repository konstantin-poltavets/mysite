from django.contrib import admin
from .models import zbdoor, zbbtn, zbtmphum
from django.template import response
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Max

#admin.site.register(zbdoor)


# Define the admin class
class ZbtmphumAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_date', 'temperature', 'humidity')
    list_filter = ('created_date',)
    change_list_template = '/home/pi/django-sendbox/mysite/templates/admin/sale_summary_change_list.html'
    date_hierarchy = 'created_date'

    def changelist_view(self, request, extra_context=None):
     
        chart_data = zbtmphum.objects.all().values('created_date', 'temperature', 'humidity')[::2]

        # Serialize and attach the chart data to the template context
        as_json = json.dumps(list(chart_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"chart_data": as_json}
       # print(extra_context)
        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)

    
# Register the admin class with the associated model
admin.site.register(zbtmphum, ZbtmphumAdmin)




@admin.register(zbbtn)
class ZbbtnAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_date', 'action', 'voltage')
    list_filter = ('created_date',)
    change_list_template = '/home/pi/django-sendbox/mysite/templates/admin/btn_change_list.html'


       
    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )
        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        
        response.context_data['summary'] = list(
            qs.values('created_date', 'action', 'id'))

        print(response.context_data['summary'])


        
        return response







@admin.register(zbdoor)
class ZbdoorAdmin(admin.ModelAdmin):
    list_display = ('topic', 'created_date', 'contact', 'voltage')
    list_filter = ('topic', 'created_date', 'contact')
    list_display_links=('topic',)
    #list_editable = ('created_date',)
