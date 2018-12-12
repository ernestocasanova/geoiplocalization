"""
Definition of models.
"""
from django.template.defaultfilters import truncatechars
from django.db import models

class RequestLogs(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='ID')
    localip = models.CharField(max_length=50, blank=True, null=True, verbose_name='IP Local')
    raw_details = models.TextField(blank=True, null=True, verbose_name='Raw Details')
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='Updated')

    @property
    def data_raw_details(self):
        return truncatechars(self.raw_details, 50)

    class Meta:
        managed = True
        db_table = 'requestlogs'
        verbose_name = 'Request Log'
        verbose_name_plural = 'Request Logs'


        