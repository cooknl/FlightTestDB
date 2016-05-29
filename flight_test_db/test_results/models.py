from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TestResult(models.Model):
    short_title = models.SlugField()
    location_description = models.CharField(max_length=30,blank=True)
    location_lat = models.DecimalField(max_digits=7,decimal_places=5,blank=True,default='0.0')
    location_lng = models.DecimalField(max_digits=8,decimal_places=5,blank=True,default='0.0')
    vehicle = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    flight_date = models.DateField()
    result_start_time = models.TimeField(blank=True)
    result_stop_time = models.TimeField(blank=True)
    test_success = models.CharField(max_length=30)
    system_evaluation = models.CharField(max_length=30)
    notes = models.TextField(blank=True)
    result_filepath = models.FilePathField(path="C:\\",allow_folders=True,allow_files=False,blank=True)




    def __unicode__(self):
        return u'%s %s' % (self.flight_date, self.short_title)
