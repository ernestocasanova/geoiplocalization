from django.contrib import admin
from app.models import RequestLogs


class RequestLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'localip', 'created', 'updated')
    search_fields = ['localip',]
    readonly_fields=('id','created', 'updated')
    order_fields = ['-id']
    list_per_page = 15

admin.site.register(RequestLogs, RequestLogsAdmin)