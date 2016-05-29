from django.contrib import admin
from test_results.models import TestResult


# Register your models here.


class TestResultAdmin(admin.ModelAdmin):
    pass

admin.site.register(TestResult, TestResultAdmin)
