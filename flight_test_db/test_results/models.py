from __future__ import unicode_literals

from django.db import models
from django.contrib.gis.db import models as gis_models

# Create your models here.
class TestResult(models.Model):
    short_title = models.SlugField()
    location_area = models.CharField(max_length=30)
    location_lat_long = gis_models.PointField(geography=True)
    vehicle = models.CharField(max_length=30)
    operator = models.CharField(max_length=30)
    flight_date = models.DateField()
    result_start_time = models.TimeField()
    result_stop_time = models.TimeField()
    test_success = models.CharField(max_length=30)
    system_evaluation = models.CharField(max_length=30)
    notes = models.TextField()
    result_filepath = models.FilePathField()


    def __unicode__(self):
        return u'%s %s' % (self.flight_date, self.short_title)
